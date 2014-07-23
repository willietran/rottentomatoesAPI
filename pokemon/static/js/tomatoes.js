/**
 * Created by WillieTran on 7/22/14.
 */

$(document).ready(function() {

    var myApiKey = 't9evbc8v4u7vgc7cu6rbxbey';

    var getMovie = function() {
        var movieContainer = $('.movieInfoContainer');
        movieContainer.html("");
        var searchQuery = $('#searchField').val();
        var pageLimit = $('#numResults').val();
        $.ajax({
        url: 'http://api.rottentomatoes.com/api/public/v1.0/' +
              'movies.json?apikey=' + myApiKey + '&q=' +
               searchQuery + '&page_limit=' + pageLimit,
        type: 'GET',
        dataType: 'jsonp',
        success: function(movie_response) {
            console.log(movie_response);
            var movies = movie_response.movies;
            var movie_list = [];
            for (i = 0; i < movies.length; i++) {
                var movie = movies[i];
                var movieInfo = {};
                movieInfo.title = movie.title;
                movieInfo.release_year = movie.year;
                movieInfo.critic_rating = movie.ratings.critics_score;
                movieInfo.poster = movie.posters.original;
                movieInfo.mpaa_rating = movie.mpaa_rating;
                movieInfo.runtime = movie.runtime;
                movieInfo.year = movie.year;
                movieInfo.audience_score = movie.ratings.audience_score;
                movie_list.push(movieInfo);
                movieContainer.append("<div class='movieItem'><img class='moviePoster'src="+movieInfo.poster+
                        "><p class='movieTitle'>"+movieInfo.title+
                        "</p><p class='movieScore'>Movie Score: "+(movieInfo.critic_rating+movieInfo.audience_score)/2.0+
                        "</p><button class='favorite' data-id="+i+">Favorite This Movie</button></p><button class='moreInfoBtn'>More Information</button>" +
                        "<div class='moreInfo' style='display:none;'><p class='mpaaRating'>MPAA Rating: "+movieInfo.mpaa_rating+
                        "</p><p class='runtime'>Runtime: "+movieInfo.runtime+"</p></div></div>");
            }

            // Toggling Information
            $('.moreInfoBtn').on('click', function() {
                $(this).text(function(i, text) {
                    return text === "More Information" ? "Less Information" : "More Information";
                });
                $(this).siblings('.moreInfo').toggle();
            });

            // Saving Favorites to the database
            $('.favorite').on('click', function() {
                var movie_id = $(this).data('id');
                var movie = movie_list[movie_id];
                movieInfo = JSON.stringify(movie);
                $(this).html("<img src='http://www.timelinecoverbanner.com/cliparts/wp-content/digital-scrapbooking/star-vector.jpg' height=50 width=auto>");
                console.log(movieInfo);
                $.ajax({
                    url: '/new_movie/',
                    type: 'POST',
                    dataType: 'html',
                    data: movieInfo,
                    success: function(response) {
                        console.log(response);
                        $('.searchResults').html(response);
                    },
                    error: function(response) {
                        console.log("error");
                    }
                });
            });
        },
        error: function(error_response) {
            console.log(error_response);
        }
        });
    };

    $('#getMovie').on('click', getMovie);

    // Saving the Movie to the database
    $('#saveMovie').on('click', function() {
        movieInfo = JSON.stringify(movieInfo);
        console.log(movieInfo);
        $.ajax({
            url: '/new_movie/',
            type: 'POST',
            dataType: 'html',
            data: movieInfo,
            success: function(response) {
                console.log(response);
                $('.movieInfoContainer').html(response);
            },
            error: function(response) {
                console.log("error");
            }
        });
    });

    // View favorites - Make an AJAX call back to the already existing hyperlink of favorites
    // and then display them.
    $('#viewFavorites').on('click', function() {
        $.ajax({
            url: '/view_favorite/',
            type: 'GET',
            dataType: 'html',
            success: function(response) {
            $('.favoriteMovies').html(response);
            $('.removeFavorite').on('click', function() {
                var movieTitle = $(this).data('title');
                movieTitle = JSON.stringify(movieTitle);
                $.ajax({
                    url: '/delete_favorite/',
                    type: 'POST',
                    dataType: 'html',
                    data: movieTitle,
                    success: function(response) {
                        console.log(response);
                        console.log("deleted");
                    },
                    error: function(response) {
                        console.log("error");
                    }
                })
            });
            },
            error: function(response) {
                console.log("error");
            }
        })
    });

});