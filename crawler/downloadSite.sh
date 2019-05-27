# page1/2100
# page2/270
# page3/340
# page4/100
# page5/230
# page6/60
# page7/120
#!/bin/bash 

# -------------------------------------------------------------------------------
# Initialization 
# -------------------------------------------------------------------------------
work_dir=`pwd`
commonLink=""
downloadRoot=false
getLinks=false
n_page=0
name=""
headle="https://batdongsan.com.vn"
while getopts ":cnmtvxk" opt; do
    case $opt in
        c)
            echo "Thue Chung Cu was triggred!"
            downloadRoot=true
            name="cho-thue-can-ho-chung-cu"
            n_page=965
            ;;
        n)
            echo "Thue nha rieng was triggred!"
            downloadRoot=true
            name="cho-thue-nha-rieng"
            n_page=270
            ;;
        m)
            echo "Thue nha mat pho was trigeered!"
            downloadRoot=true
            name="cho-thue-nha-mat-pho"
            n_page=340
            ;;
        t)
            echo "Thue nha tro was trigeered!"
            downloadRoot=true
            name="cho-thue-nha-tro-phong-tro"
            n_page=100
            ;;
        v)
            echo "Thue van phong was trigeered!"
            downloadRoot=true
            name="cho-thue-van-phong"
            n_page=230
            ;;
        k)
            echo "Thue cua hang was trigeered!"
            downloadRoot=true
            name="cho-thue-cua-hang-ki-ot"
            n_page=60
            ;;
        x)
            echo "Thue xuong was trigeered!"
            downloadRoot=true
            name="cho-thue-kho-nha-xuong-dat"
            n_page=120
            ;;
        # g)
        #     echo "get links was triggered"
        #     getLinks=true
        #     ;;
        \?)
            echo "Invalid option: -$OPTARG"
            ;;
    esac
done
function download_root_page {
    mkdir -p ${work_dir}/ROOT_PAGE/${name}
    page=1
    while [ $page -le $n_page ]
    do
        link="${headle}/${name}/p${page}"
        wget -c -nv --timeout=15 --tries=5 --waitretry=1 -U"${USERAGENT_ARR[$u_a]}" --random-wait --keep-session-cookies --save-cookies=${work_dir}/ROOT_PAGE/${name}/cookies.$$ ${link} -O ${work_dir}/ROOT_PAGE/${name}/page-${page}.html
        let "page=page+1"
    done
}
function get_detail {
    dir=${work_dir}/PRODUCT/${name}
    c=1
    n_page=`ls ${dir} | grep -c html`
    printf "link\ttitle\tlocation\timage\tarea\tprice\n" > ${work_dir}/${name}.csv
    printf "detail\n" > ${work_dir}/${name}_detail.csv
    while [ ${c} -le ${n_page} ]
    do  
        awk -f ${work_dir}/get_infomation.awk ${dir}/page-${c}.html >> ${work_dir}/${name}.csv
        awk -f ${work_dir}/get_detail.awk ${dir}/page-${c}.html >> ${work_dir}/${name}_detail.csv
        let "c=c+1"
    done    
}
function get_product_links {
    mkdir -p ${work_dir}/PRODUCT/${name}
    page=1
    while [ ${page} -lt ${n_page} ]
    do 
        awk -f ${work_dir}/get_links.awk ${work_dir}/ROOT_PAGE/${name}/page-${page}.html >> ${work_dir}/PRODUCT/${name}/links.tab
        let "page=page+1"
    done
}
function download_list_mode_page {
    file=${work_dir}/PRODUCT/${name}/links.tab
    page=1
    while IFS= read line
    do
        link="${line}"
        wget -c -nv --timeout=15 --tries=5 --waitretry=1 -U"${USERAGENT_ARR[$u_a]}" --random-wait --keep-session-cookies --save-cookies=${work_dir}/PRODUCT/${name}/cookies.$$ ${link} -O ${work_dir}/PRODUCT/${name}/page-${page}.html
        # printf '%s\n' "${link}"
        let "page=page+1"
    done <"$file"
}
if ${downloadRoot}
then
    echo "Download root mode is on"
    # download_root_page
    # get_product_links
    # download_list_mode_page
    get_detail
    # download_image
    # get_color
    # write_to_csv
fi 