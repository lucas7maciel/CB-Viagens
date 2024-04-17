<script lang="ts">
import IconProfile from '@/components/icons/IconProfile.vue';

export default {
    props: ["user"],
    components: {
        IconProfile
    }
}

</script>

<template>
    <div class="container">
        <div class="profile">
        <IconProfile class="pic" />
    </div>
    <p class="name">{{ user.first_name }} {{ user.last_name }}</p>
    <p class="since">Desde ontem</p>
    </div>
</template>

<style scoped>
.container {
    text-align: center;

    padding: 1rem 0;
}

.profile {
    max-height: 8rem;
    max-width: 8rem;
    aspect-ratio: 1;

    margin: 0 auto 0.5rem auto;

    border-radius: 50%;
    border: solid 3px white;
    box-shadow: 0 0 3px rgba(0, 0, 0, 0.2);

    background-color: gray;

    overflow: hidden;
}

.profile .pic {
    max-width: 100%;
    max-height: 100%;

    object-fit: contain;
}

.name {
    font-weight: bold;
    font-size: 2rem;

    color: black;
}

.since {
    font-weight: semibold;
    font-size: 1.4rem;

    color: rgb(59, 59, 59);
}
</style>