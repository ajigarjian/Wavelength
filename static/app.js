
//javascript function for dragging the dial. Guidance taken from here: https://www.petercollingridge.co.uk/tutorials/svg/interactive/dragging/
function makeDraggable(evt) {

    //sets the elements in the svg as the target of the event
    var svg = evt.target;

    //links functions created below with mouse events so that when you click the dial the functionality for dragging triggers
    svg.addEventListener('mousedown', startDrag);
    svg.addEventListener('mousemove', drag);
    svg.addEventListener('mouseup', endDrag);
    svg.addEventListener('mouseleave', endDrag);

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

    // function getLineLength(evt) {

    //     x1 = selectedElement.getAttributeNS(null, "x1");
    //     x2 = selectedElement.getAttributeNS(null, "x2");

    //     y1 = selectedElement.getAttributeNS(null, "y1");
    //     y2 = selectedElement.getAttributeNS(null, "y2");

    //     length = Math.sqrt(Math.pow((x1 - x2),2) + Math.pow((y1 - y2),2))

    //     return {
    //         length
    //     };
    // }

    // checks if the element has the CSS class 'draggable', if it does, it sets it to be the 'selectedElement'
    function startDrag(evt) {
        if (evt.target.classList.contains('draggable'))
        {
            selectedElement = evt.target;

            offset = getMousePosition(evt);
            offset.x -= parseFloat(selectedElement.getAttributeNS(null, "x2"));
            offset.y -= parseFloat(selectedElement.getAttributeNS(null, "y2"));
        }
    }

    function drag(evt) {

        //will only be true if the selectedElement is no longer false/empty after startDrag function is performed
        if (selectedElement) {

            evt.preventDefault();

            // gets x and y coordinate of mouse
            var mousePos = getMousePosition(evt);

            //gets x value of element and stores in variable x, then sets it to be original x coordinate + 0.1
            selectedElement.setAttributeNS(null, "x2", mousePos.x-offset.x);
            selectedElement.setAttributeNS(null, "y2", mousePos.y-offset.y);
            
        }
    }

    //stops the element from moving once the mouse has been released
    function endDrag(evt) {
        selectedElement = null;
    }
}
