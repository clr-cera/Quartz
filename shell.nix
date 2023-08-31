{ pkgs ? import <nixpkgs> {} }:

let
    my-python-packages = ps: with ps; [ 
      # For dns translation
      dnspython
    ];
  in

pkgs.mkShell {
  name = "ICMChat";
  nativeBuildInputs = with pkgs.buildPackages; [
    (pkgs.python3.withPackages my-python-packages)

  ]; 
}
