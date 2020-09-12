set -gx EULER_DIR \
	(realpath (dirname (realpath (pwd)/(status --current-filename)))/../..)

. $EULER_DIR/venv/bin/activate.fish

set -gx DATA_DIR "$EULER_DIR/data"
set -gx CACHE_DIR "$EULER_DIR/cache"

set -gx DESK_DIR "$EULER_DIR/desk"
set -gx DRAWER_DIR "$EULER_DIR/drawer"
set -gx SOLVED_DIR "$EULER_DIR/solved"

set -gx _OLD_EULER_PATH $PATH
set -gx _OLD_EULER_PYTHONPATH $PYTHONPATH

set -gx PATH "$EULER_DIR/bin" $PATH
set -gx PYTHONPATH "$EULER_DIR/lib" $PYTHONPATH

functions -c deactivate venv_deactivate
functions -e deactivate

function deactivate
	if test -n "$_OLD_EULER_PATH"
		set -gx PATH $_OLD_EULER_PATH
		set -e _OLD_EULER_PATH
	end
	if test -n "$_OLD_EULER_PYTHONPATH"
		set -gx PYTHONPATH $_OLD_EULER_PYTHONPATH
		set -e _OLD_EULER_PYTHONPATH
	end

	set -e DATA_DIR
	set -e CACHE_DIR

	set -e DESK_DIR
	set -e DRAWER_DIR
	set -e SOLVED_DIR

	functions -e deactivate

	functions -c venv_deactivate deactivate
	functions -e venv_deactivate

	deactivate
end
