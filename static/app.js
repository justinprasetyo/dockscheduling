const vessel_length = document.getElementById("vessellength")
const vessel_width = document.getElementById("vesselwidth")
const vessel_length_enterbtn = document.getElementById("enter-btn-vessellengthwidth")

const dock_name = document.getElementById("dockname")

const start_date = document.getElementById("startdate")
const end_date = document.getElementById("enddate")

vessel_length_enterbtn.addEventListener('click', async () => {
    const response = await fetch('/api/dimensions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            length: vessel_length.value,
            width: vessel_width.value
        })
    });

    const result = await response.json()
    console.log(result)
    console.log(dock_name.value)
    console.log(`${start_date.value}, ${end_date.value}`)
}) 