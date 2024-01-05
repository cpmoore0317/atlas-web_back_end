// cpmoore0317

import ClassRoom from './0-classroom.js';

export default function initializeRooms() {
  const maxSize = [19, 20, 34];
  return maxSize.map(function(size) {
    return new ClassRoom(size);
  });
}
