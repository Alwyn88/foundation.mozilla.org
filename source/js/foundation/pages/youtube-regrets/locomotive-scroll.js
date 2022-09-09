import LocomotiveScroll from "locomotive-scroll";

export const initYoutubeRegretsLocomotiveScroll = () => {
  const locoScroll = new LocomotiveScroll({
    el: document.querySelector(".scroll-container"),
    smooth: true,
    repeat: true,
    mobile: {
      smooth: true,
      breakpoint: 0,
    },
    tablet: {
      smooth: true,
      breakpoint: 0,
    },
  });

  // Make sure loco scroll is up to date after page has totally finished laoding
  var interval = setInterval(function () {
    if (document.readyState === "complete") {
      clearInterval(interval);
      locoScroll.update();
    }
  }, 100);
};
