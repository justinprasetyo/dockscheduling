const vessel_length = document.getElementById("vessellength")
const vessel_length_enterbtn = document.getElementById("enter-btn-vessellength")

vessel_length_enterbtn.addEventListener('click', async () => {
    const response = await fetch('/api/dimensions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            length: vessel_length.value
        })
    });

    console.log(response)
}) 