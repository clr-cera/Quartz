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
            default = ICMChatComplete;

            ICMChatComplete = pkgs.python3Packages.buildPythonApplication rec {
              format = "pyproject";
              name = "ICMChat";
              src = ./.;
              propagatedBuildInputs = [ (pkgs.python3.withPackages my-python-packages) ];
            };

            

          };
          
        }
      );
}
