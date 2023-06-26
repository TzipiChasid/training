
factorial()
{

    if [ $1 -gt $2 ]
    then
        rs=`expr $i % 2`
        echo rs
        if [ rs -eq 0 ]
        then
            echo $1
            factorial $(($1 + 2)) $2  
        fi
        factorial $(($1 + 1)) $2 
    fi
 
}

factorial



