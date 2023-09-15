{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils}:
    flake-utils.lib.eachDefaultSystem
      (system:
        let
          inherit (nixpkgs.lib) getExe;

          pkgs = import nixpkgs {
            inherit system;
          };

          my-python-packages = ps: with ps; [ 
          dnspython
          build
          setuptools
          ];
          
        in rec
        {
          packages = rec {
            default = Quartz;

            Quartz = pkgs.python3Packages.buildPythonApplication {
              format = "pyproject";
              name = "Quartz";
              pname = "Quartz";
              src = ./.;
              propagatedBuildInputs = [ (pkgs.python3.withPackages my-python-packages) ];
            };

            Server =  pkgs.writeShellScriptBin "Quartz-Server" ''
              python ${Quartz}/lib/python3.10/site-packages/Quartz/server.py
            '';
          };
          apps = {
            default = {
              type = "app";
              program ="${packages.Quartz}/bin/Quartz";
            };
            
            Server = {
              type = "app";
              program =getExe packages.Server;
            };

          };
          
        }
      );
}
