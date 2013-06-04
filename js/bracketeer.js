goog.require('goog.dom');
goog.require('goog.ui.TabBar');

function makeTabs() {
  var tabBar = new goog.ui.TabBar();
  tabBar.decorate(goog.dom.getElement('tabs_main'));
}

