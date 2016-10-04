ui_folder=ui_files
output=ui

export_file() {
    file=$1;
    filename="${file#$ui_folder/}";
    filename="${filename%.*}";
    filename="$output/$filename";
    echo Exporting $1 to $filename.py;
    mkdir -p $(dirname "$filename");
    pyuic5 $1 > $filename.py;
}

export_directory() {
    for i in $1/*
    do
        if test -f "$i"
        then
            export_file $i;
        elif test -d "$i"
        then
            export_directory $i;
        fi
    done
}

export_directory $ui_folder;