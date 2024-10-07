document.addEventListener("DOMContentLoaded", function() {
    const disciplinaField = document.getElementById('id_disciplina');
    const assuntoField = document.getElementById('id_assunto');

    function filterAssuntos() {
        const disciplinaId = disciplinaField.value;
        for (let i = 0; i < assuntoField.options.length; i++) {
            const option = assuntoField.options[i];
            if (option.getAttribute('data-disciplina-id') == disciplinaId || option.value === "") {
                option.style.display = 'block';
            } else {
                option.style.display = 'none';
            }
        }
    }

    // Filter assuntos on page load
    filterAssuntos();
	console.log('Testando!')
    // Filter assuntos when the disciplina field changes
    disciplinaField.addEventListener('change', filterAssuntos);
});
