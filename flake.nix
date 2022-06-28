{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    futils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, futils } @ inputs:
    let
      inherit (nixpkgs) lib;
      inherit (lib) recursiveUpdate;
      inherit (futils.lib) eachDefaultSystem defaultSystems;

      nixpkgsFor = lib.genAttrs defaultSystems (system: import nixpkgs {
        inherit system;
      });
    in
    (eachDefaultSystem (system:
      let
        pkgs = nixpkgsFor.${system};
      in
      {
        devShell = pkgs.mkShell {
          buildInputs = with pkgs; [
            git
            hugo
          ];
        };
      }
    ));
}
