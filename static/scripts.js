document.getElementById('upload-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const response = await fetch('/upload', {
        method: 'POST',
        body: formData,
    });
    const result = await response.json();
    console.log(result);
});
