BEGIN{
    detail=""
}
/class="pm-desc"/{
    getline
    # gsub(/<br\/>+/,";;;",$0)
    detail=rtrim($0)   
}
END{
    print(detail)
}
function rtrim(s){
    gsub(/\r+/,"", s);
    gsub(/\t+/,"", s); 
    gsub(/\n+/,"", s); 
    return s 
}