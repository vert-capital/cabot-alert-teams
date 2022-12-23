from cabot_alert_teams.template import TemplatesMixin


def test_template_read_template():
    obj = TemplatesMixin()
    response = obj._read_template("tests/mocks/template.html")

    assert response == "<b>$name</b>"


def test_template_render():
    obj = TemplatesMixin()
    response = obj.render("tests/mocks/template.html", name="Thiago")

    assert response == "<b>Thiago</b>"
