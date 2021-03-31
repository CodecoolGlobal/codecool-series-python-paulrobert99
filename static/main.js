let base_url = "/api/top/"
let current_page = 1

let init = {

    getShows:function(page=current_page){
        let table = document.querySelector("#table_")
        table.innerHTML=""
        fetch(base_url+page)
        .then(response =>response.json())
        .then(data=>this.render_table(data))




    },
    render_table:function(data){
        let table = document.querySelector("#table_")
        for (show of data[0].json_agg){
            let row = document.createElement("tr")

            let title = document.createElement("td")
            let release = document.createElement("td")
            let runtime = document.createElement("td")
            let rating = document.createElement("td")
            let genres = document.createElement("td")
            let homepage = document.createElement("td")
            let trailer = document.createElement("td")

            let video = document.createElement("a")
            let link_homepage = document.createElement("a")

            trailer.append(video)
            homepage.append(link_homepage)

            title.textContent= show.title
            release.textContent= show.release
            runtime.textContent= show.runtime
            rating.textContent= parseFloat(show.rating).toFixed(1)
            genres.textContent= show.genres

            link_homepage.setAttribute("href", show.homepage)
            link_homepage.textContent = "Homepage"

            video.setAttribute("href",show.trailer )
            video.textContent = "Trailer"
            if(show.trailer==null){
                trailer.removeChild(video)
                trailer.textContent= "No URL"
            }
            if(show.homepage==null){
                homepage.removeChild(link_homepage)
                homepage.textContent="Not avaliable"
            }
            row.append(title,release,runtime,rating,genres,trailer,homepage)
            table.append(row)
        }


    },

    setButtons:function(){
        $("#next_button").click(function(){
            if (current_page<66){
                $("#next_button").disabled=false
                init.getShows(++current_page)
                
                
            }else{
                $("#next_button").disabled=true
                
            }
        })
        $("#prev_button").click(function(){
            if (current_page==1){
                $("#prev_button").disabled=true
                
                
            }else{
                $("#prev_button").disabled=false
                init.getShows(--current_page)
                
            }
        })
    }

}

window.onload= function(){
    init.getShows()
    init.setButtons()
}