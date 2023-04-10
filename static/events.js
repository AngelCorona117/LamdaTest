function loadHomePage() {
    if (window.location.pathname === '/') {

        //grab every graph 
        let graphs = document.querySelectorAll(".item");
        //get buttons
        let buttons = document.querySelectorAll(".btn");
        //hambuger menu
        let navBtn = document.querySelector("#select-display");
        //hamburger menu options
        let navOptions = document.querySelector(".display-option");
        //avg and total div
        const avgAndTotal = document.querySelector("#avgORtotal");
        //get images
        const images = document.querySelectorAll('.item img');

        //!!!!!!!!!IGNORE THIS PART!!!!!!!!!!!!!
        //FUNCTIONS:  (HELPERS FUNCTIONS)
        function display_tables(...items) {
            //hide everything
            for (let graph of graphs) {
                if (!graph.classList.contains("hidden")) {
                    graph.classList.add("hidden");
                }
            }
            //show only the items you want
            for (let item of items) {
                graphs[item].classList.remove("hidden");
            }
            return items;
        }

        function add_event_listener_to_button(button, ...items) {
            buttons[button].addEventListener("click", () => {
                items = display_tables(...items);

                // Display avg and total options
                if (avgAndTotal.classList.contains("hidden")) {
                    avgAndTotal.classList.remove("hidden");
                }

                //button to show the averange of the graphs selected
                buttons[5].addEventListener("click", () => {
                    //hide everything
                    for (let graph of graphs) {
                        if (!graph.classList.contains("hidden")) {
                            graph.classList.add("hidden");
                        }
                    }
                    //show only the items that contain the word averange
                    for (let item of items) {

                        let src = images[item].getAttribute("src");
                        const fileName = src.split('/').pop();

                        if (fileName.includes('averange')) {
                            graphs[item].classList.remove("hidden");
                        }
                    }
                });
                //button to show the total of the graphs selected
                buttons[6].addEventListener("click", () => {
                    //hide everything
                    for (let graph of graphs) {
                        if (!graph.classList.contains("hidden")) {
                            graph.classList.add("hidden");
                        }
                    }
                    //show only the items that contain the word total
                    for (let item of items) {

                        let src = images[item].getAttribute("src");
                        const fileName = src.split('/').pop();

                        if (fileName.includes('total')) {
                            graphs[item].classList.remove("hidden");
                        }
                    }
                });
            });
        }

        //!!!!!!!!!THE IMPORTANT EVENTS GOES HERE!!!!!!!!!!!!!
        //togle the hamburger menu option
        navBtn.addEventListener("click", () => {
            navOptions.classList.toggle("hidden");
        });

        //button 0 its the show all button
        buttons[0].addEventListener("click", () => {
            for (let graph of graphs) {
                if (graph.classList.contains("hidden")) {
                    graph.classList.remove("hidden");
                }
            }
            //hide avg and total options
            if (!avgAndTotal.classList.contains("hidden")) {
                avgAndTotal.classList.add("hidden");
            }
        });
        //first argument is the button number,the  second argument (and everything after that) are the images you want to display
        add_event_listener_to_button(1, 4, 5);
        add_event_listener_to_button(2, 0, 1, 2, 3);
        add_event_listener_to_button(3, 6, 7);
        add_event_listener_to_button(4, 8, 9, 10, 11, 12, 13, 14, 15);
    }
}

document.addEventListener('DOMContentLoaded', loadHomePage);
