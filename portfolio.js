let activePageId = "about-me_wrapper";
jQuery(`#${activePageId}`).addClass("active-page");
jQuery(`#${activePageId}_a`).addClass("active");

const handlePage = (id) => {
  jQuery(`#${activePageId}`).removeClass("active-page");
  jQuery(`#${id}`).addClass("active-page");
  jQuery(`#${activePageId}_a`).removeClass("active");
  jQuery(`#${id}_a`).addClass("active");
  activePageId = id;
};
