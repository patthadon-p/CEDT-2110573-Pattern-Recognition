# Directory for auxiliary files
$aux_dir = '.build';

# Create directory if it does not exist
if ( ! -d $aux_dir ) {
    mkdir $aux_dir or die "Cannot create $aux_dir: $!";
}

# Latex engines
$pdflatex = "pdflatex -synctex=1 -interaction=nonstopmode -file-line-error -aux-directory=$aux_dir %O %S";
$lualatex = "lualatex -synctex=1 -interaction=nonstopmode -file-line-error -aux-directory=$aux_dir %O %S";
$xelatex  = "xelatex  -synctex=1 -interaction=nonstopmode -file-line-error -aux-directory=$aux_dir %O %S";

# Default engine
$latex = $pdflatex;

# Let latexmk emulate aux dir behavior properly
$emulate_aux = 1;

# Files we consider generated
@generated_exts = qw(
aux bbl blg fdb_latexmk fls log out toc lot lof
synctex.gz nav snm vrb
);

# Clean unnecessary files after build
$cleanup_includes_generated = 1;

# Custom clean rule (keeps aux + dependency files)
$clean_ext .= " %R.synctex.gz %R.log %R.out %R.nav %R.snm %R.vrb";