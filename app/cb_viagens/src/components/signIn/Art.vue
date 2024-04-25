<template>
  <div class="svg_section">
    <img class="art" src="../../assets/Planes/plane2.gif" />
  </div>
</template>

<style scoped>
/** Container */
.svg_section {
  flex: 1 1 50%;

  display: flex;
  align-items: center;
  justify-content: center;

  background-color: #cceaf7;
  
  overflow: hidden;
  white-space: nowrap;

  animation: init_svg 0.8s;
}

.svg_section .art {
  max-width: 100%;
  max-height: 100%;

  object-fit: contain;
}

/** Animations */
@keyframes init_svg {
  from {
    flex: 0;
  }
  to {
    flex: 1 1 50%;
  }
}
</style>
