from pic_project.spbackstage.qt_backstage import QTBackstage


if __name__ == '__main__':
    uids = ['379445']

    qtbackstage = QTBackstage()
    qtbackstage.pic_material(uids[0], 2)
