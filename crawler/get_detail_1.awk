BEGIN{
    area[""]=0
    location[""]=0
    images[""]=0
    price[""]=0
    links[""]=0
    title[""]=0
    c=0
    g=0
    i=0
    headle="https://batdongsan.com.vn"
}
/vip0 search-productItem/{
    if  (length($0) != 0){
        getline
        getline
        c++
        split($0,arr,"href='")
        split(arr[2],link,"'")
        links[c]=headle""link[1]
        split($0,arr1,"title='")
        split(arr1[2],t,"'")
        title[c]=ltrim(t[1])
    }
}
/vip1 search-productItem/{
    if  (length($0) != 0){
        getline
        getline
        c++
        split($0,arr,"href='")
        split(arr[2],link,"'")
        links[c]=headle""link[1]
        split($0,arr1,"title='")
        split(arr1[2],t,"'")
        title[c]=ltrim(t[1])
    }
}
/vip2 search-productItem/{
    if  (length($0) != 0){
        getline
        getline
        c++
        split($0,arr,"href='")
        split(arr[2],link,"'")
        links[c]=headle""link[1]
        split($0,arr1,"title='")
        split(arr1[2],t,"'")
        title[c]=ltrim(t[1])
    }
}
/vip3 search-productItem/{
    if  (length($0) != 0){
        getline
        getline
        c++
        split($0,arr,"href='")
        split(arr[2],link,"'")
        links[c]=headle""link[1]
        split($0,arr1,"title='")
        split(arr1[2],t,"'")
        title[c]=ltrim(t[1])
    }
}
/vip4 search-productItem/{
    if  (length($0) != 0){
        getline
        getline
        c++
        split($0,arr,"href='")
        split(arr[2],link,"'")
        links[c]=headle""link[1]
        split($0,arr1,"title='")
        split(arr1[2],t,"'")
        title[c]=ltrim(t[1])
    }
}
/vip5 search-productItem/{
    if  (length($0) != 0){
        getline
        getline
        c++
        split($0,arr,"href='")
        split(arr[2],link,"'")
        links[c]=headle""link[1]
        split($0,arr1,"title='")
        split(arr1[2],t,"'")
        title[c]=ltrim(t[1])
    }
}
/product-avatar-img/{
    i++
    split($0,arr,"src=\"")
    split(arr[2],image,"\"")
    sub(/crop/,"resize",image[1])
    sub(/350x232/,"745x510",image[1])
    if (image[1] == "/Images/nophoto.jpg"){
        images[i]= headle"/Images/nophoto.jpg"
    }
    else{
        images[i]=image[1]
    }
        
}
/product-price/{
    g++
    split($0,arr,"\">")
    split(arr[2],p,"</")
    price[g]=p[1]
    getline
    getline
    #area
    split($0,arr1,"\">")
    split(arr1[2],a,"</")
    area[g]=a[1]
    getline
    getline
    getline
    #location
    location[g]=$0
}
END{
    max_c=c
    for(c=1;c<=max_c;c++){
        print(links[c]"\t"title[c]"\t"price[c]"\t"area[c]"\t"images[c]"\t"location[c])
    }
}
# -image
# -location
# -giá
# -title
#-  area
# -links
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
    gsub(/^[ \-\;\t\r\n]/, "", s); 
    return s 
}
