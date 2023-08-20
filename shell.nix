{ pkgs ? import <nixpkgs> {} }:

let
    my-python-packages = ps: with ps; [ 
      # For dns translation
      dnspython
    ];
  in

pkgs.mkShell {
  # nativeBuildInputs is usually what you want -- tools you need to run
  nativeBuildInputs = with pkgs.buildPackages; [
    (pkgs.python3.withPackages my-python-packages)

  ]; 
}
