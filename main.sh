if [ $# -lt 2 ]
    then
        echo "Nonogram path and file must be specified"
else
    python src/main.py $1 $2
fi

