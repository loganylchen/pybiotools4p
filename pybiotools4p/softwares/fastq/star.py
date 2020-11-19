# AUTOGENERATED! DO NOT EDIT! File to edit: 03_star.ipynb (unless otherwise specified).

__all__ = ['Star']

# Cell

from ..base import Base, modify_cmd


# Cell

class Star(Base):
    def __init__(self, software, fd):
        super(Star, self).__init__(software)
        self._default = fd

    def cmd_version(self):
        return 'echo {repr};{software} --version'.format(
            repr=self.__repr__(),
            software=self._software
        )

    @modify_cmd
    def cmd_build_index(self, star_index_dir, reference, gtf, read_length):
        '''
        :param star_index_dir:
        :param reference:
        :param gtf:
        :param read_length:
        :return:
        '''
        return r'''
{star} {build_index} \
        --genomeDir {star_index_dir} \
        --genomeFastaFiles {reference} \
        --sjdbGTFfile {gtf} \
        --sjdbOverhang {read_length}
        '''.format(
            star=self._software,
            build_index=self._default['build_index'],
            **locals()
        )

    @modify_cmd
    def cmd_align(self, star_idx, fq1, fq2, prefix, gtf, read_length, miRNA=False):
        '''
        :param star_idx:
        :param fq1:
        :param fq2:
        :param prefix:
        :param gtf:
        :param sampleid:
        :param lane:
        :param platform:
        :param read_length:
        :return:
        '''

        return r'''
{star} {align_paras} \
    --genomeDir {star_idx} \
    --readFilesIn {fq1} {fq2} \
    --outFileNamePrefix {prefix} \
    --sjdbGTFfile {gtf}  \
    --sjdbOverhang {read_length} {mp}
            '''.format(
            star=self._software,
            align_paras=self._default['align'],
            mp=self._default['mirna_align'] if miRNA else '',
            **locals()
        )

    def __repr__(self):
        return 'star:' + self._software

    def __str__(self):
        return 'Spliced Transcripts Alignment to a Reference'