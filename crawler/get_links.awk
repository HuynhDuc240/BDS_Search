BEGIN{
    links[""]=0
    c=0
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
    }
}
END{
    max_c=c
    for(c=1;c<=max_c;c++){
        print(links[c])
    }
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
    gsub(/^[ \-\;\t\r\n]/, "", s); 
    return s 
}
