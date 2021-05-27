#!/bin/bash

##Example :: sh convert_vio_folder_toBag.sh /our_nas/20210526_101_CarPark

echo "請輸入要轉檔的資料夾路徑（內部全是raw data的上一層）: $1"

for i in $1/* ; do
  if [ -d "$i" ]; then
    #echo "$i"
    #echo $(basename "$i")
    kalibr_bagcreater --folder $i --output-bag $i/$(basename "$i").bag
  fi
done

