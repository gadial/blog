// Function to initialize the graph with data
function initializeGraph(data) {
    console.log(data);
    const cy = cytoscape({
        container: document.getElementById('graph-container'),

        style: [
            {
                selector: 'node',
                style: {
                    'label': 'data(name)',
                    'width': 300,
                    'height': 200,
                    'background-color': '#0074D9',
                    'color': '#ffffff',
                    'text-valign': 'center',
                    'text-halign': 'center',
                    'font-size': '20px',
                    'border-width': 2,
                    'border-color': '#001f3f',
                    'text-wrap': 'wrap',
                    'text-max-width': 280, // Adjust max width as needed
                }
            },
            {
                selector: 'edge',
                style: {
                    'width': 3,
                    'line-color': '#aaaaaa',
                    'target-arrow-color': '#aaaaaa',
                    'target-arrow-shape': 'triangle'
                }
            }
        ],

        layout: {
            name: 'grid',
            rows: 1
        },

        zoomingEnabled: true,
        userZoomingEnabled: true,
        minZoom: 0.1,
        maxZoom: 10,
        wheelSensitivity: 0.2
    });

    // Add nodes to the graph
    data.posts.forEach(post => {
        cy.add({
            group: 'nodes',
            data: { id: post.id, name: post.name }
        });
    });

    // Add edges to the graph
    data.links.forEach(link => {
        console.log(link);
        cy.add({
            group: 'edges',
            data: { id: `${link.source}-${link.target}`, source: link.source, target: link.target }
        });
    });

    // Initialize a layout
    cy.layout({
        name: 'cose',
        animate: true
    }).run();

    // Enable zooming with D3
    const zoom = d3.zoom().on('zoom', (event) => {
        cy.zoom(event.transform.k);
        cy.pan({ x: event.transform.x, y: event.transform.y });
    });

    d3.select('#graph-container').call(zoom);
}

// Fetch the JSON data and initialize the graph
fetch('site_map.json')
    .then(response => response.json())
    .then(data => initializeGraph(data))
    .catch(error => console.error('Error loading JSON data:', error));
