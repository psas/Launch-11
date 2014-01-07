# Countodwn Clock

# inject context into a function that is othewise called globally
proxy = (fn, context) ->
    p = -> fn.apply(context)
    return p

#format object on string
if !String.prototype.format
    String.prototype.format = ->
        args = arguments
        this.replace(/{(\d+)}/g, (match, number) ->
            if typeof args[number] != 'undefined' then args[number] else match
        )

# Countdown class
class window.Counter

    timer: ->

    run = ->
        now = new Date()
        diff = Math.abs(@date - now)
        days  = Math.floor( diff / 8.64e7)
        hours = Math.floor((diff % 8.64e7) / 36e5)
        mins  = Math.floor((diff % 36e5)   / 6e4)
        secs  = Math.floor((diff %  6e4)   / 1000)
        tuesdays = Math.floor( diff / 6.048e8 )
        tuesdays = if now.getDay() < 2 then tuesdays+1 else tuesdays
        @node.innerHTML = @fmt.format(days, hours, mins, secs, tuesdays)

    constructor: (datestr, @node, @fmt, @interval) ->
        @date = new Date(datestr)

    start: ->
        proxy(run, @)()
        clearInterval @timer
        @timer setInterval(proxy(run, @), @interval*1000)

    stop: ->
        clearInterval @timer
