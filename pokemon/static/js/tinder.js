/**
 * Created by WillieTran on 7/23/14.
 */

$(document).ready(function() {

    var myApiKey = 't9evbc8v4u7vgc7cu6rbxbey';
    var movieID;

    movie_list = [];
    $('#submitBtn').on('click', function() {
        var query = $('#search').val();
        var pageLimit = 3;
        var movieID;
        var isSuccessful;

        $.ajax({
            url: 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey='+ myApiKey +'&q='+ query +'&page_limit='+ pageLimit,
            type: 'GET',
            dataType: 'jsonp',
            success: function(response) {
                console.log(response.movies[0].id);
                movieID = response.movies[0].id;
            },
            error: function(response) {
                console.log(response);
            }
        }).complete(function() {
            $.ajax({
                url: 'http://api.rottentomatoes.com/api/public/v1.0/movies/'
                    + movieID +'/similar.json?apikey=' + myApiKey + '&limit=5',
                type: 'GET',
                dataType: 'jsonp',
                success: function(response) {
                    console.log("Similar:");
                    console.log(response);
                    console.log("printing self link...");
                    for (i = 0; i < response.movies.length; i++) {
                        movie = response.movies[i];
                        movieInfo = {};
                        movieInfo.title = movie.title;
                        movieInfo.poster = movie.posters.original;
                        movieInfo.identifier = movie.id;
                        var movieLink = response.movies[i].links['self'];
                        movie_list.push(movieInfo);
                        $('#recommended').append("<div><p>"+ response.movies[i].title +"</p><button id='learnMore' data-id="
                                                +movieLink+">Learn More</button><button class='favoriteBtn' data-id="+ i +">favorite</button><div class='synopsis'></div></div>");
                        console.log(movieLink);
                    }
                },
                error: function(response) {
                    console.log(response);
                }
            })
        });
    });
    $(document).on('click', '.favoriteBtn', function() {
        console.log("Favorite Button Pressed");
        var favID = $(this).data('id');
        var favMovie = movie_list[favID];
        var favoriteMovie = JSON.stringify(favMovie);
        console.log(favoriteMovie);
        $.ajax({
            url: '/new_favorite/',
            type: 'POST',
            dataType: 'html',
            data: favoriteMovie,
            success: function(response) {
                console.log(response);
//                $('.movieInfoContainer').html(response);
            },
            error: function(response) {
                console.log("error");
            }
        });

    });

    $(document).on('click', '#learnMore', function() {
        console.log("Learn More Button Pressed");
        selfLink = $(this).data('id');
        synopDest = $(this).parent();
        console.log(selfLink);
        $.ajax({
            url: selfLink + '?apikey=' + myApiKey,
            type: 'GET',
            dataType: 'jsonp',
            success: function(response) {
                console.log("Printing...");
                console.log(response);
                console.log("Printing synopsis");
                console.log("Synopsis: " +response.synopsis);
                synopDest.append(response.synopsis);
                synopDest.append("<br><img src='"+response.posters.original+"'><hr>");
            },
            error: function(response) {
                alert("error");
            }
        })
    })
});
