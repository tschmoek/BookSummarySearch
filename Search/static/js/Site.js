
$(document).ready(function(){
    $('#test').click(function(e) {
        var query = $('#id_searchval').val()
        if(!query){
            console.log('EMPTY')
            $('#id_searchval').appendTo('<br><span class="help-inline">Something may have gone wrong</span>')
            return
        }
        if ($('#searchResults'))
            $('#searchResults').empty()
        $(".sk-fading-circle").fadeIn(1000)

        $.get("/searchQuery/" + query, function(data, status){
            $(".sk-fading-circle").hide()
            if(data.RegexError){
                $('#searchResults').append('<div class="has-error">'+data.RegexError+'</div>')
            }
            if(data.EmptyError){
                
            }
            if (data.goodlist != null){
                $('#searchResults').append('<div class="row">'+
                '<div class="col-md-3"></div> '+
                '<div class="col-md-5">'+
                    '<h3>Good Reads</h3>'+
                    '<a target="_blank" href='+data.goodlist+'>Link</a>'+
                    '<br>'+
                '</div>'+
            '</div>')
            }
            if (data.actionlist != null){
                $('#searchResults').append('<div class="row">'+
                '<div class="col-md-3"></div> '+
                '<div class="col-md-5">'+
                    '<h3>Actionable Books</h3>'+
                    '<a target="_blank" href='+data.actionlist+'>Link</a>'+
                    '<br>'+
                '</div>'+
            '</div>') 
            }
            if (data.fourmin != null){
                $('#searchResults').append('<div class="row">'+
                '<div class="col-md-3"></div>'+
                '<div class="col-md-5">'+
                    '<h3>Four Minute</h3>'+
                     '<a target="_blank" href='+data.fourmin+'>Link</a>'+
                    '<br>'+
                '</div>'+
            '</div>')
            }
            if (data.overdrivelist != null){
                $('#searchResults').append('<div class="row">'+
                '<div class="col-md-3"></div>'+
                '<div class="col-md-5">'+
                    '<h3>Overdrive Library</h3>'+
                    '<a target="_blank" href='+data.overdrivelist+'>Link</a>'+
                    '<br>'+
                '</div>'+
            '</div>')
            }
            if (data.blink != null){
                $('#searchResults').append('<div class="row">'+
                '<div class="col-md-3"></div>'+
                '<div class="col-md-5">'+
                    '<h3>Blink</h3>'+
                    '<a target="_blank" href='+data.blink+'>Link</a>'+
                    '<br>'+
                '</div>'+
            '</div>')
            }

            if (data.bizsum != null){
                $('#searchResults').append('<div class="row">'+
                '<div class="col-md-3"></div>'+
                '<div class="col-md-5">'+
                    '<h3>Biz Summaries</h3>'+
                    '<a target="_blank" href='+data.bizsum+'>Link</a>'+
                    '<br>'+
                '</div>'+
            '</div>')
            }
            if (data.kirkus != null){
                $('#searchResults').append('<div class="row">'+
           '<div class="col-md-3"></div>'+
                '<div class="col-md-5">'+
                    '<h3>Kirkus Reviews</h3>'+
                    '<a target="_blank" href='+data.kirkus+'>Link</a>'+
                    '<br>'+
                '</div>'+
            '</div>')
            }
            if (data.readit != null){
                $('#searchResults').append('<div class="row">'+
                '<div class="col-md-3"></div>'+
                '<div class="col-md-5">'+
                    '<h3>Read It for Me</h3>'+
                    '<a target="_blank" href="https://readitfor.me/">Link</a>'+
                    '<br>'+
                '</div>'+
            '</div>')
            }

            if (data.youtubelist != null){
                // data.youtubelist.forEach(function(element) {
                //     console.log(element)
                // }, this);
                if (data.youtubelist.length == 3){
                    $('#searchResults').append('<div class="row">'+
                        '<h3 class="text-center">Youtube Results</h3>'+
                        '<div class="col-md-4"><iframe width="95%" height="300px" src='+data.youtubelist[0]+'></iframe></div> '+
                        '<div class="col-md-4"><iframe width="95%" height="300px" src='+data.youtubelist[1]+'></iframe></div>'+
                        '<div class="col-md-4"><iframe width="95%" height="300px" src='+data.youtubelist[2]+'></iframe></div>'+
                    '</div>')
                }
                if (data.youtubelist.length == 2){
                    $('#searchResults').append('<div class="row">'+
                        '<h3 class="text-center">Youtube Results</h3>'+
                        '<div class="col-md-4"><iframe width="95%" height="300px" src='+data.youtubelist[0]+'></iframe></div> '+
                        '<div class="col-md-4"><iframe width="95%" height="300px" src='+data.youtubelist[1]+'></iframe></div>'+
                    '</div>')
                }
                if (data.youtubelist.length == 1){
                    $('#searchResults').append('<div class="row">'+
                        '<h3 class="text-center">Youtube Results</h3>'+
                        '<div class="col-md-4"><iframe width="95%" height="300px" src='+data.youtubelist[0]+'></iframe></div> '+
                    '</div>')
                }
            }
            

            });
        });
});
