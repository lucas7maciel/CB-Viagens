<template>
  <div class="svg_section">
    <img class="art" src="../../assets/Planes/plane2.gif" />
  </div>
</template>

<style scoped>
.svg_section {
  flex: 1 1 50%;
  display: flex;
  align-items: center;
  justify-content: center;

  background-color: #cceaf7;
  overflow: hidden;

  animation: init_svg 0.8s;

  /*Ajeitar*/
  white-space: nowrap;
}

.svg_section .art {
  max-width: 100%;
  max-height: 100%;

  object-fit: contain;
}

@keyframes init_svg {
  from {
    flex: 0;
  }
  to {
    flex: 1 1 50%;
  }
}
</style>
