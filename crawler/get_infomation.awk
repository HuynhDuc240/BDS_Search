BEGIN{
    title[""]=0
    t=0
    location[""]=0
    l=0
    price[""]=0
    p=0
    area[""]=0
    a=0
    headle="https://batdongsan.com.vn/"
    link[""]=0
    image[""]=0
}
/method="post"/{
    c++
    split($0,arr,"action=\"")
    split(arr[2],arr1,"\"")
    link[c]=headle""arr1[1]
}
c=0
/itemprop="name"/{
    getline
    t++
    title[t]=rtrim($0)
}
/diadiem-title mar-right-15/{
    getline
    l++
    split($0,arr,"\">")
    split(arr[2],arr1,"</span>")
    gsub("</a>","",arr1[1])
    location[l]=ltrim(arr1[1])
}
/gia-title mar-right-15/{
    getline
    getline
    getline
    getline
    p++
    gsub("&nbsp;","",$0)
    price[p]=rtrim($0)
}
/class="gia-title"/{
    getline
    getline
    getline
    getline
    a++
    split($0,arr,"</")
    area[a]=rtrim(arr[1])
}
c=0
/class="photo"/{
    getline
    getline
    c++
    split($0,arr,"src=\"")
    split(arr[2],arr1,"\"")
    image[c]=rtrim(arr1[1])
}
END{
    max_t=t
    for(i=1;i<=max_t;i++){
        print(link[i]"\t"title[i]"\t"location[i]"\t"image[i]"\t"area[i]"\t"price[i])
    }
}
function rtrim(s){
    sub("\r", "", s);
    sub(/\t+/, "", s); 
    return s 
}
function ltrim(s){ 
    gsub("&#192;","À",s)
    gsub("&#202;","Ê",s)
    gsub("&#225;","á",s)
    gsub("&#244;","ô",s)
    gsub("&#243;","ó",s)
    gsub("&#242;","ò",s)
    gsub("&#234;","ê",s)
    gsub("&#237;","í",s)
    gsub("&#224;","à",s)
    gsub("&#193;","Á",s)
    gsub("&#250;","ú",s)
    gsub("&#249;","ù",s)
    gsub("&#212;","Ô",s)
    gsub("&#195;","Ã",s)
    gsub("&#226;","â",s)
    gsub("&#245;","õ",s)
    gsub("&#233;","é",s)
    gsub("&#194;","Â",s)
    gsub("&#236;","ì",s)
    gsub("&#227;","ã",s)
    gsub("&#253;","ý",s)
    gsub("&#39;","'",s)
    gsub("&#232;","è",s)
    gsub("&#221;","Ý",s)
    gsub("&#205;","Í",s)
    gsub("&#210;","Ò",s)
    gsub("&#218;","Ú",s)
    gsub(/^[0-9]+./,"",s)
    gsub(/^[ \-\;\t\r\n]/,"", s); 
    return s 
}