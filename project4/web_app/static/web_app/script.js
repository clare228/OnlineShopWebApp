document.addEventListener('DOMContentLoaded', () => {
    
    // Side navigation 
    if (document.querySelector('#open_nav')){
        document.querySelector('#open_nav').onclick = () => {
            document.getElementById("mySidenav").style.width = "250px";
        }
    }
    if (document.querySelector('#close_nav')){
        document.querySelector('#close_nav').onclick = () => {
            document.getElementById("mySidenav").style.width = "0";
        }
    }

    // Logo = homepage
    document.querySelector('#logo').onclick = () =>{
        window.location.href = '.';
    }

    // Category image links
    if (document.querySelector('.category_img')){
        document.querySelectorAll('.category_img').forEach(image =>{
            image.onclick = () => {
                console.log(image.id)
                window.location.href = image.id;
            }
        });
    }

    // Collapsible filters
    if (document.querySelector('.collapsible')){
        var coll = document.getElementsByClassName("collapsible");
        var i;

        for (i = 0; i < coll.length; i++) {
            coll[i].addEventListener("click", function() {
                this.classList.toggle("active");
                var content = this.nextElementSibling;
                if (content.style.maxHeight){
                    content.style.maxHeight = null;
                } else {
                    content.style.maxHeight = content.scrollHeight + "px";
                } 
            });
        }
    }

    // function to filter item colours
    function fliter_items(db, colour_id, display_opt){// set or item db, colour filter chosen, display or not (string)
        document.querySelectorAll('.item_div').forEach(item =>{
            
            for (j=0; j<db.length; j++){
                if(db[j]['pk'].toString() === item.id){ // find div item in db
                    item_colours=db[j]['fields']['colour'];
                    console.log(db[j]['fields']['item_name'] + ': ' + item_colours)
                    count = 0;
                    for (k=0; k<item_colours.length; k++){ // for each item colour
                        if(item_colours[k].toString()===colour_id){ //if colour matches selected colour
                            count = count+1
                        }
                    }
                    if (count===0){ // item has no matching colours to selected colour
                        item.style.display= display_opt;
                    }
                }
            }
            
        })
    }

    // function to filter set colours
    function fliter_sets(db, colour_id, display_opt){
        document.querySelectorAll('.set_div').forEach(item =>{
            console.log(db)
            for (j=0; j<db.length; j++){
                if(db[j]['pk'].toString() === item.id){ // find div item in db
                    set_colours=db[j]['fields']['set_colour'];
                    console.log(db[j]['fields']['set_name'] + ': ' + set_colours)
                    count = 0;
                    for (k=0; k<set_colours.length; k++){ // for each item colour
                        if(set_colours[k].toString()===colour_id){ //if colour matches selected colour
                            count = count+1
                        }
                    }
                    if (count===0){ // item has no matching colours to selected colour
                        item.style.display= display_opt;
                    }
                }
            }
            
        })
    }

    // Check colours to filter
    if (document.querySelector('.colour_check')){
        if (document.querySelector('.item_div') || document.querySelector('.set_div')){
            document.querySelectorAll('.colour_check').forEach(box =>{
                
                box.onchange = () =>{
                    if (box.checked){
                        colour_id = box.id;
                        fliter_items(items, colour_id, "none");
                        fliter_sets(sets, colour_id, "none");

                    }else if (box.checked === false){
                        console.log(box.id + 'not checked')
                        colour_id = box.id;
                        fliter_items(items, colour_id, "flex");
                        fliter_sets(sets, colour_id, "flex");

                        // Check if other boxes are checked
                        document.querySelectorAll('.colour_check').forEach(box_2 =>{
                            if (box_2.checked){
                                colour_id = box_2.id;
                                fliter_items(items, colour_id, "none");
                                fliter_sets(sets, colour_id, "none");
                            }
                        })

                    }

                }
            })
        }
    }

    // function to filter item price
    function fliter_price_items(db, min_price, max_price){
        document.querySelectorAll('.item_div').forEach(item =>{
            
            for (j=0; j<db.length; j++){
                if(db[j]['pk'].toString() === item.id){ // find div item in db
                    item_price=db[j]['fields']['price'];
                    
                    if (item_price < min_price || item_price > max_price){
                        item.style.display= "none";

                    }else{
                        item.style.display= "flex"

                    }
                }
            }
            
        })
    }

    // function to filter set price
    function fliter_price_sets(db, min_price, max_price){
        document.querySelectorAll('.set_div').forEach(item =>{

            min_price = parseInt(min_price)
            max_price = parseInt(max_price)
            
            for (j=0; j<db.length; j++){
                if(db[j]['pk'].toString() === item.id){ // find div item in db
                    set_price=db[j]['fields']['set_price'];
                    
                    if (set_price < min_price || set_price > max_price){
                        item.style.display= "none";
                        
                    }else{
                        item.style.display= "flex"
                    }
                }
            }
            
        })
    }

    // filter price
    if (document.querySelector('.filter_price')){

        document.querySelector('#price_form').onsubmit = () => {

            let min_price = document.querySelector('#min_price').value
            let max_price = document.querySelector('#max_price').value

            console.log(min_price)
            console.log(max_price)

            if (min_price === ""){
                min_price = "0";
                console.log('no min')
            };

            if (max_price === ""){
                max_price = "1000";
                console.log('no max')
            };

            if (parseInt(max_price)-parseInt(min_price) < 0){
                price_temp = min_price;
                min_price = max_price;
                max_price = price_temp;
                console.log('min>max')
            };

            if (max_price === min_price){
                max_price = parseInt(max_price) + 10;
                max_price = max_price.toString()
                min_price = parseInt(min_price) - 10;
                min_price = min_price.toString()
                console.log('min=max')
            }

            fliter_price_sets(sets, min_price, max_price)
            fliter_price_items(items, min_price, max_price)            

            return false;
        }
    }


    // function for item image --> item page
    function item_page (set_or_item, db){
        if (document.querySelector(`.${set_or_item}_div`)){
            document.querySelectorAll(`.${set_or_item}_div`).forEach(div =>{
                div.onclick = () =>{
                    for (j=0; j<db.length; j++){
                        if(db[j]['pk'].toString() === div.id){
                            item_name = db[j]['fields'][`${set_or_item}_name`];
                            item_id = db[j]['pk'];
                            item_type = set_or_item;
                        }
                    }
                    window.location.replace("http://127.0.0.1:8000/" + item_name + "/" + item_type + "/" + item_id);
                }
            });
        }
    }

    // sets and items to individual page
    item_page('set', sets);
    item_page('item', items);

    // Choose other colours on item page
    if (document.querySelector('#colour_drop')){
        document.querySelector('#colour_drop').onchange = () =>{
            let val = document.querySelector('#colour_drop').value

            for (j=0; j<items.length; j++){
                if(items[j]['pk'].toString() === val){
                    item_name = items[j]['fields']["item_name"];
                    item_id = items[j]['pk'];
                    item_type = "item";
                }
            }
            window.location.replace("http://127.0.0.1:8000/" + item_name + "/" + item_type + "/" + item_id);
        }
    }
})