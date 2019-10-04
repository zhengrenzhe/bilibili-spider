function toGBSize(size) {
    return `${(size / Math.pow(1024, 3) || 0).toFixed(2)}GB`;
}

export {toGBSize};