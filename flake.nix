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
          ];
        in

        with pkgs;
        {
          devShells.default = mkShell {
            buildInputs = [
            (pkgs.python3.withPackages my-python-packages)
            ];
          };
        }
      );
}
