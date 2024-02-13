#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce(
    (acc, e) => {
      return (e === searchElement) ? ++acc : acc;
    }, 0
  );
};
