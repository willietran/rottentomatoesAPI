/**
 * Created by WillieTran on 7/21/14.
 */

$(document).ready(function() {

    var pokemon_list = [];
    var pokemon = {};
    var printPokemon = function(randomNum, classStatus) {
//        for (var i = 0; i < 6; i++) {
            var pokeNum = Math.floor(Math.random() * 719) + 2;
            $.ajax({
                url: "http://pokeapi.co/api/v1/sprite/" + randomNum,
                type: "GET",
                dataType: "jsonp",
                success: function (data) {
                    pokemon.name = data.pokemon.name;
                    pokemon.id = data.id - 1;
                    pokemon.image = "http://pokeapi.co" + data.image;
                    pokemon_list.push(data);
                    var cart = $('#cart');
                    cart.append("<div class='pokeTeam'></div>");
                    pokeTeam = $('.pokeTeam');
                    pokeTeam.last().append("<div class='pokeHolder'></div>");
                    pokeHolder = $('.pokeHolder');
                    pokeHolder.last().append("<p id='"+pokemon.id+"'># "+ pokemon.id + '</p>');
                    pokeHolder.last().append("<img class='pokeImage' src="+ pokemon.image + '/>');
                    pokeHolder.last().append("<p class='pokeName'>"+ pokemon.name + '</p>');
                    pokeHolder.addClass(classStatus);
                    console.log(data);
                    console.log(pokemon_list);
                    console.log(pokemon);
                }
            });
//        }
    };

    $('.randomTeam').on('click', function(){
        $('#cart').html("");
        for (var i = 0; i < 6; i++){
            $('randomTeam').on('click', printPokemon(Math.floor((Math.random() * 719) + 1), 'active'));
        }
    });

    $('.save-team').on('click', function(){
        pokemon = JSON.stringify(pokemon_list);
        $.ajax({
            url: '/new_pokemon/',
            type: 'POST',
            dataType: 'json',
            data: pokemon,
            success: function(response) {
                console.log(response);
            },
            error: function(response) {
                console.log(response)
            }
        })
    });

    // Catch them all
    $('.pokeMatch').on('click', function() {
        $('#cart').html("");
        var pokeList = [];
        // Creates six random numbers and pushes two of them into my empty array
        for (var i = 0; i < 6; i++) {
            randomNum = Math.floor((Math.random() * 719) + 1);
            pokeList.push(randomNum, randomNum);
        }
        // Randomly sorts my array
        pokeList.sort(function() {
            return .5 - Math.random();
        });
        // Prints my array
        for (var j = 0; j < pokeList.length; j++) {
            printPokemon(pokeList[j], 'inactive');
        }

    });

    // Click Toggle For classStatus
    var active = $('.active');
    var pokeList = [];

    $(document).on('click', '.pokeTeam', function() {

        if (pokeList.length < 2 && $(this).children().hasClass('inactive')) {
            $(this).children().addClass('active');
            $(this).children().removeClass('inactive');
            pokeList.push($(this).children().children());
            console.log(pokeList.length)
        }
        if (pokeList.length === 2) {
            if (pokeList[0].attr('id') === pokeList[1].attr('id')) {
                pokeList[0].addClass('matched');
                pokeList[1].addClass('matched');
                pokeList = [];
            } else {
                console.log("Try again");
                pokeList[0].parent().removeClass('active').addClass('inactive');
                pokeList[1].parent().removeClass('active').addClass('inactive');
                pokeList = [];
            }

        }


    });


});
