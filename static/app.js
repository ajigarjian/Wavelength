function makeDraggable(evt) {

    //sets the elements in the svg as the target of the event
    var svg = evt.target;

    //links functions created below with mouse events so that when you click the dial the functionality for dragging triggers
    svg.addEventListener('mousedown', startDrag);
    svg.addEventListener('mousemove', drag);
    svg.addEventListener('mouseup', endDrag);
    svg.addEventListener('mouseleave', endDrag);
    window.addEventListener('resize', dialReset);

    //initialize an empty selected element
    var selectedElement = false;
    
    //helper function to get the position of the mouse, details unnecessary to know. 
    function getMousePosition(evt) {
        var CTM = svg.getScreenCTM();

        return {
          x: (evt.clientX - CTM.e) / CTM.a,
          y: (evt.clientY - CTM.f) / CTM.d
        };
    }

    // checks if the element has the CSS class 'draggable', if it does, it sets it to be the 'selectedElement'
    function startDrag(evt) {
        if (evt.target.classList.contains('draggable'))
        {
            selectedElement = evt.target;
        }
    }

    //resizes all the dials when the window is resized. Snaps movable dial to upright position and then moves the scoring lines to the correct location
    function dialReset() {

        //getting the winning degree from the html from the backend
        winning_degree=parseFloat(document.getElementById("winning_deg").getAttributeNS(null, "value"));

        //getting current svvg height and width (width happens to be width of window)
        var windowWidth = window.outerWidth;   
        var windowHeight = parseFloat((document.getElementById("dial_svg")).getAttributeNS(null, "height"));

        //getting the radius of the half circle as a percentage of the svg's height and width
        var radiusPercentage = (parseFloat((document.getElementById("outer_circle")).getAttributeNS(null, "r")))/100.0;
        //for figuring out how percentages work as svg attributes: https://oreillymedia.github.io/Using_SVG/extras/ch05-percentages.html
        var circleRadius = radiusPercentage*(Math.sqrt(Math.pow(windowWidth, 2) + Math.pow(windowHeight, 2))/Math.SQRT2);

        //reset dial to be in upright position whenever window is resized
        document.getElementById("dial").setAttributeNS(null, "x2", windowWidth*0.5);
        document.getElementById("dial").setAttributeNS(null, "y2", (windowHeight - circleRadius));

        //reset length of scoring lines when window is resized by taking into account the svg height minus the new circle radius
        document.getElementById("middle_line").setAttributeNS(null, "y2", (windowHeight - circleRadius));
        document.getElementById("left_orange").setAttributeNS(null, "y2", (windowHeight - circleRadius));
        document.getElementById("right_orange").setAttributeNS(null, "y2", (windowHeight - circleRadius));
        document.getElementById("left_yellow").setAttributeNS(null, "y2", (windowHeight - circleRadius));
        document.getElementById("right_yellow").setAttributeNS(null, "y2", (windowHeight - circleRadius));

        //reset angle of scoring lines to make sure they stay consistent with new window parameters
        document.getElementById("middle_line").setAttributeNS(null, "transform", "rotate(" + winning_degree + " " + windowWidth/2 + " 250)");
        document.getElementById("left_orange").setAttributeNS(null, "transform", "rotate(" + (winning_degree-3) + " " + windowWidth/2 + " 250)");
        document.getElementById("right_orange").setAttributeNS(null, "transform", "rotate(" + (winning_degree+3) + " " + windowWidth/2 + " 250)");
        document.getElementById("left_yellow").setAttributeNS(null, "transform", "rotate(" + (winning_degree-6) + " " + windowWidth/2 + " 250)");
        document.getElementById("right_yellow").setAttributeNS(null, "transform", "rotate(" + (winning_degree+6) + " " + windowWidth/2 + " 250)");

    }

    function drag(evt) {

        //will only be true if the selectedElement is no longer false/empty after startDrag function is performed
        if (selectedElement) {

            evt.preventDefault();

            // gets x and y coordinate of mouse
            var mousePos = getMousePosition(evt);

            //getting the values of the svg width, height, and circle radius as absolute values from percentages in html
            var windowWidth = window.outerWidth;
            var windowHeight = parseFloat((document.getElementById("dial_svg")).getAttributeNS(null, "height"));
            var radiusPercentage = (parseFloat((document.getElementById("outer_circle")).getAttributeNS(null, "r")))/100.0
            //for figuring out how percentages work as svg attributes: https://oreillymedia.github.io/Using_SVG/extras/ch05-percentages.html
            var circleRadius = radiusPercentage*(Math.sqrt(Math.pow(windowWidth, 2) + Math.pow(windowHeight, 2))/Math.SQRT2)
            
            //stores location of mouse x coordinate in pixels
            var newX = mousePos.x;

            //setting upper limit of x when moving dial
            if (newX > ((windowWidth*0.5)+circleRadius)) {
                newX = ((windowWidth*0.5)+circleRadius)-0.01;
            }

            //setting lower limit of x when moving dial
            else if (newX < ((windowWidth*0.5)-circleRadius)) {
                newX = ((windowWidth*0.5)-circleRadius)+0.01;
            }

            //sets x2 attribute of selectedElement (in this case the line) to be the new X
            selectedElement.setAttributeNS(null, "x2", newX);

            //creates variable to store what the new y should be based on d = square root of ((x2-x1)^2 + (y2-y1)^2)
            var newY = windowHeight-Math.sqrt((Math.pow(circleRadius,2) - Math.pow((newX - windowWidth*0.5),2)))

            //sets y2 attribue of selectedElement (in this case the line) to be the new Y
            selectedElement.setAttributeNS(null, "y2", newY)
        }
    }
   
    //stops the element from moving once the mouse has been released
    function endDrag(evt) {
        selectedElement = null;

    }
}

//this shows the scorecard
window.onload = function(){

    //when the button with id refresher_reveal is clicked..
    refresher_reveal.addEventListener('click',touch);
    
    //run this function..
    function touch(){
        //store the item with ID revealer to a variable..
        var revealer = document.getElementById('revealer'); 
        //and then hide it..
        revealer.style.visibility="hidden";
        }       
    }

//this shows the scorecard
window.onload = function(){

    //when the button with id refresher_hider is clicked..
    refresher_hider.addEventListener('click',touch);
    
    //run this function..
    function touch(){
        //store the item with ID revealer to a variable..
        var hider = document.getElementById('hider'); 
        //and then hide it..
        hider.setAttributeNS(null, "hidden", no);
        }       
    }