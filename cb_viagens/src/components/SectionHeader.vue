
<template>
  <div class="title">
    <h1><slot></slot></h1>
  </div>
</template>

<style scoped>
/** Container */
.title {
  flex: 0;

  display: flex;
  justify-content: center;
  align-items: center;

  padding: 0.5rem;
  margin-bottom: 1rem;

  background-color: var(--primary-color);
  border-radius: 1rem;
  color: white;

  user-select: none;
}

.title h1 {
  font-weight: bold;
}

/** Queries */
@media (max-width: 900px) {
  .title {
    display: none;
  }
}
</style>
