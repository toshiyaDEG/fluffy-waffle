//Create the observer
const observer = new IntersectionObserver(entries => {
    // Loop over the entries
    entries.forEach(entry => {
        //If the element is visible
        if (entry.isIntersecting) {
            //Tell the observer which elements to track
            entry.target.classList.add('animate-fade');
            entry.target.classList.add('animate-pop');
            return;
        }
        // We're not intersecting, so remove the class!
        entry.classList.remove('animate-fade');
        entry.classList.remove('animate-pop');
    });
});

observer.observe(document.querySelector('.animate'));