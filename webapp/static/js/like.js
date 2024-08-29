document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.like-button').forEach(function (button) {
        button.addEventListener('click', function () {
            let postId = this.dataset.postId;
            fetch(`/api/posts/${postId}/like/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            }).then(response => response.json())
                .then(data => {
                    if (data.status === 'like toggled') {
                        let likeCountElement = document.querySelector(`#like-count-${postId}`);
                        likeCountElement.textContent = data.likes_count;
                    }
                });
        });
    });
});
