/**
 * Created by amaridev on 08.07.17.
 */

// Module for task list:
var taskList = (function() {

    //get items
    (function() {
        $.ajax({
            url: '/list',
            type: 'get',
            success: function(r) {
                r.forEach(function(entry) {
                    addItemToList(entry)
                });
                addCheckedEvent();
                addCloseEvent();
            }
        })
    }());


    var addCloseEvent = function() {
        // Add Close button to items and bind click event
        $('.close').each(function() {
            $(this).unbind('click').on('click', function(e){
                e.stopPropagation();
                var $target = $(this).closest('li');
                var id = $target.data('id');

                $.ajax({
                    url: '/delete',
                    type: 'POST',
                    data: JSON.stringify({'id': id}),
                    success: function () {
                        $target.hide();
                    }
                })
            });
        });
    };

    var addCheckedEvent = function() {
        // Add a "checked" symbol when clicking on a list item
        $('#todo-list').unbind().on('click', function(e) {
            var $clicked = $(e.target).closest('li');
            $clicked.toggleClass('checked');

            var data = !!$clicked.hasClass('checked');

            $.ajax({
                url: '/update',
                type: 'post',
                dataType: 'json',
                data: JSON.stringify({'id': $clicked.data('id'), 'state': data}),
                error: function() {
                    // undo checked since ajax failed
                    $clicked.toggleClass('checked');
                }
            })

        });
    };


    var addItemToList = function(item) {
        // Render item into the list
        var checked = item['state'] ? 'checked' : '';
        $('#todo-list').append(
            $('<li>').data('id', item['id']).addClass(checked).append(
                $('<span>').addClass('title').text(item['title'])
            ).append(
                $('<span>').addClass('desc').text(item['description'])
            ).append(
                $('<span>').addClass('due').text(new Date(item['due']).toLocaleDateString())
            ).append(
                $('<span>').addClass('close').text('\u00D7')
            ));
    };

    (function() {
        // On add-todo form submit, add item to list
        $('#add-todo').submit(function(e) {
            e.preventDefault();
            $.ajax({
                url: '/add',
                type: 'post',
                dataType: 'json',
                data: JSON.stringify($(this).serializeArray().reduce(function(a, x) { a[x.name] = x.value; return a; }, {})),
                success: function(res) {
                    addItemToList(res['added']);
                    addCheckedEvent();
                    addCloseEvent();
                    $('#add-todo')[0].reset()
                }
            });
        });
    }());

    // Allow filtering of todo-list
    (function() {
        $('#list-search').on('keyup change', function () {
            clearTimeout(thread);
            var $this = $(this);
            var thread = setTimeout(function(){

                var search = $this.val();
                var regex = new RegExp(search.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&'), 'i');

                $('#todo-list').find('li').each(function () {
                    var li = $(this);
                    if (search.length === 0) {
                        li.show();
                        return;
                    }

                    var val = li.find('.title').text();
                    if ( val.search(regex) !== -1) {
                        li.show();
                    } else {
                        li.hide();
                    }
                });
            }, 100);
        });
    })();

});

$(document).ready(function(){
    taskList();
});