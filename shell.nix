with import <nixpkgs> {};

stdenv.mkDerivation {
  name = "python-env";
  buildInputs = [
    python313
    uv
  ];
}
