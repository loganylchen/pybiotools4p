# AUTOGENERATED! DO NOT EDIT! File to edit: 01_fastp.ipynb (unless otherwise specified).

__all__ = ['Fastp']

# Cell

from ...base import Base,modify_cmd

# Cell

class Fastp(Base):
    def __init__(self, software, fd):
        super(Fastp, self).__init__(software)
        self._default = fd

    def cmd_version(self):
        '''
        :return:
        '''
        return 'echo {repr} ;{software} --version'.format(
            repr=self.__repr__(),
            software=self._software
        )

    @modify_cmd
    def cmd_clean_data(self, fq1, cfq1, fq2, cfq2, report_prefix):
        '''
        :param fq1:
        :param cfq1:
        :param fq2:
        :param cfq2:
        :param report_prefix:
        :return:
        '''

        if fq2 in ['',None]:
            return r'''
{software} {se} \
        -i {fq1} \
        -o {cfq1} \
        --html {report_prefix}.fastp.html \
        --json {report_prefix}.fastp.json
            '''.format(
                se=self._default['se'],
                software=self._software,
                **locals()
            )
        else:
            return r'''
{software} {pe} \
        -i {fq1} \
        -I {fq2} \
        -o {cfq1} \
        -O {cfq2} \
        --html {report_prefix}.fastp.html \
        --json {report_prefix}.fastp.json
            '''.format(
                pe=self._default['pe'],
                software=self._software,
                **locals())

    def __repr__(self):
        return 'fastp:' + self._software

    def __str__(self):
        return 'A tool designed to provide fast all-in-one preprocessing for FastQ files. This tool is developed ' \
               'in C++ with multithreading supported to afford high performance.'