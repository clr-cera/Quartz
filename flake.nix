{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils}:
    flake-utils.lib.eachDefaultSystem
      (system:
        let
          pkgs = import nixpkgs {
            inherit system;
          };

          my-python-packages = ps: with ps; [ 
          dnspython
          build
          ];
        in

        with pkgs;
        {
          devShells.default = mkShell {
            name = "ICMChat";
            buildInputs = [
            (pkgs.python3.withPackages my-python-packages)
            ];
          };

          packages = rec {
            default = ICMChatClient;

            ICMChatClient = pkgs.python3Packages.buildPythonApplication rec {
              format = "pyproject";
              name = "ICMChat";
              src = ./ICMChat;
              propagatedBuildInputs = [ (pkgs.python3.withPackages my-python-packages) ];
            };

          };
        }
      );
}
