# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:06:37 2023

@author: GuptaR
"""




from SPARQLWrapper import SPARQLWrapper, XML, JSON, TURTLE, CSV
import requests
import time
import pandas as pd
import os
import sys


from rdflib import Graph, Literal, RDF, URIRef, BNode, Namespace #basic RDF handling
from rdflib import URIRef











import requests

print('insert_canonical_formulas_in_nomad')

headers = {
    'Content-Type': 'application/sparql-update',
}

data = "PREFIX hybrid3:<https://materials.hybrid3.duke.edu/materials/> PREFIX matvoc:<http://stream-ontology.com/matvoc-core/> INSERT DATA {  matvoc:mat_H4I3NSn_5GtoP8hRMTumn5BdRjRIz2KmQhqE hybrid3:has_canonical_formula matvoc:NH4SnI3.\
    matvoc:mat_H4I3NSn_5t5UAGHT7IiC_5xHQOPLGtJr4GQg hybrid3:has_canonical_formula matvoc:NH4SnI3.\
    matvoc:mat_H4I3NSn_74HvXZGCKjmSO6EqNnI_g6NIRybd hybrid3:has_canonical_formula matvoc:NH4SnI3.\
      matvoc:mat_H4I3NSn_8stpfIPNKDYOBXEZfCiwo0zx7-fQ hybrid3:has_canonical_formula matvoc:NH4SnI3.\
      matvoc:mat_H4I3NSn_9RTICR94OwIZtLP9GvO__5_jJ0NR hybrid3:has_canonical_formula matvoc:NH4SnI3.\
      matvoc:mat_H4I3NSn_A7dsIk5t1fdhrtYZkE5qRVVgLPQ6 hybrid3:has_canonical_formula matvoc:NH4SnI3.\
    matvoc:mat_H4I3NSn_CGjml8uMtvaQeG80Rrd1nsHEdEsO hybrid3:has_canonical_formula matvoc:NH4SnI3.\
    matvoc:mat_H4I3NSn_DEfGEi-OkUrVzFxJpwcIQQV_CbMR hybrid3:has_canonical_formula matvoc:NH4SnI3.\
    matvoc:mat_H4I3NSn_R8FPQWf_-3DKXxHmnqImSo4Be1NO hybrid3:has_canonical_formula matvoc:NH4SnI3.\
    matvoc:mat_H4I3NSn_SryfCgNfSzLkUTWhTtSaXg_CA0nA hybrid3:has_canonical_formula matvoc:NH4SnI3.\
    matvoc:mat_H4I3NSn_U-vmGNCz-HCnrt3Am0DTEGOQtbD5 hybrid3:has_canonical_formula matvoc:NH4SnI3.\
  matvoc:mat_H4I3NSn_VEVuWioZK4rVePtfvlL3Z2CNA4t5 hybrid3:has_canonical_formula matvoc:NH4SnI3.\
    matvoc:mat_H4I3NSn_WquVr6Kz8ozKGlGPcXvarbZJdQB5 hybrid3:has_canonical_formula matvoc:NH4SnI3.\
      matvoc:mat_H4I3NSn_XMSWSgNkvzth0LiplVCNKDbgTo47 hybrid3:has_canonical_formula matvoc:NH4SnI3.\
      matvoc:mat_H4I3NSn_XcQum__URK5o-36WHKnWDhOF7IuO hybrid3:has_canonical_formula matvoc:NH4SnI3.\
    matvoc:mat_H4I3NSn__Uk4KzdxnB-pXwtiPsFsqC5nG_Ighybrid3:has_canonical_formula matvoc:NH4SnI3.\
    matvoc:mat_H4I3NSn__irtejxyx6pjKa2fBz5IaEaBLHT4 hybrid3:has_canonical_formula matvoc:NH4SnI3.\
      matvoc:mat_H4I3NSn_dzJjLOa4ZzFQuWJUfqhDcrzkHpbw hybrid3:has_canonical_formula matvoc:NH4SnI3.\
  matvoc:mat_H4I3NSn_i0lDKg57ZvSd1seUOzevzdYhD2Ov hybrid3:has_canonical_formula matvoc:NH4SnI3.\
matvoc:mat_H4I3NSn_mKtSnoMiULqs37w9j4ZsU7N2NEC6 hybrid3:has_canonical_formula matvoc:NH4SnI3.\
    matvoc:mat_H4I3NSn_p2p5DbVK3HYJmZictSNgNzpShJl2 hybrid3:has_canonical_formula matvoc:NH4SnI3.\
     matvoc:mat_H4I3NSn_rmgnidxtZE7zZZAWryTWyUSfqytF hybrid3:has_canonical_formula matvoc:NH4SnI3.   matvoc:mat_H4I3NSn_sLt8QR7A6GyjwtO010IeWuvryC35 hybrid3:has_canonical_formula matvoc:NH4SnI3.\
       matvoc:mat_H4I3NSn_tcMB0a7ifyVXBSgmnKj1-4w3XX21 hybrid3:has_canonical_formula matvoc:NH4SnI3.\
       matvoc:mat_CH6Br3GeN_5Zhy4ZxzqZk-jheF3RXlQ6-j8wjD hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_5Zhy4ZxzqZk-jheF3RXlQ6-j8wjD hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_88OxGoWJnJ-kEn3UssRgBxKi9Wz3 hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_98FdrKisJyOBJcjoUiImyX1sItAs hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_AdT5rdaIP0xTpTd67kYumT1M4QSj hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_AkgW6DC4fejLt8xXSKpoYyNJLLm_ hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_DJ_Jxi2K_sijlq-Yo2uCuKtI9YjA hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_EPGSwuwMabAgtt-UZh_grY8rZbEY hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_GIJAZ2tFqDPbsBooxmvglUnAgfFy hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_Gj2JbqreSHFCaa3aSRiX7WZipDrU hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_H-UcTgFyZvzjYKLW9SjHIiV-OpLe hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_Ja21yOdQmCtzX6quUGuclOOr5YsS hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_Jw1jiCDYOb5cLF7HlEj-DSuX33hD hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_L_B-PXSjhfLhclVZzp5dAq3x6G_d hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_NvjmqnWbAU5Y3UOCGr5tuxSbFz5d hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_P4aehyyI5JYd944WQ4ib_Ge_OxoI hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_P8_SSRF9zTAGKtWYBt97yC4FsBpS hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_SgRtUE-c6nUuePe5Ug8MYjmUqhMg hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_TwLDmaYczHk5GFfDN2YPLt9iMiWM hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_U3pGABdWnvSRk_v7rAimGCK0-gFv hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_Wg_E-cP0eLT0Yze_VJ2oV_n3vKL3 hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_aZVRj3uBRFL4slHt3krK8FfQqWx_ hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_bQZvu7cJem7AGAd3zcJVs4hhM0tP hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_b_mbxaJMlwDc0hqkG8SgmwyCT6KZ hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_gtYUrTtzwFobZdLbjSuVxGr_QXce hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_h4TfUyKCONaLgSi5jy6VeHlP2rv0 hybrid3:has_canonical_formula matvoc:CH6NGeBr3. matvoc:mat_CH6Br3GeN_hcbtlYOddaUil8CYJwTLJBxLeKTR hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_hpuPxDic0LgPKIY6_fWlP8XQpu9J hybrid3:has_canonical_formula matvoc:CH6NGeBr3. matvoc:mat_CH6Br3GeN_lCLMGJ7_B_7jUAufiqNaK1FluxeI hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_n4p5qR3n0o4-eFhBNvWPm7vWz3BQ hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_nsVRQdaEw9qbYmKjL43jAOUHdauh hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_pOOraVuVg2DMSp1UD6flY3oalv9w hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_qD46xJUE5sDq4f0P-xdC4ZwkB9mm hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_sRCaOWKL9cnY7UFGMu7l_2v_Ef11 hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_vFdu24syS3f6vWyghYhAD3KZMWJC hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH6Br3GeN_vsWt8RyjYjXHKqUXDscdO564SzKL hybrid3:has_canonical_formula matvoc:CH6NGeBr3.\
matvoc:mat_CH5Br3N2Pb_3mMuRJiKLlfqJ3tmzwPfgl_M0y9P hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
matvoc:mat_CH5Br3N2Pb_5GOtCgMIpyxxop8FgiubrYMytHvU hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
matvoc:mat_CH5Br3N2Pb_8kmtSqhs4Vzrv40vbGxpSlKaY0bM hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
matvoc:mat_CH5Br3N2Pb_9H6gjdnXZfBb1mGGjJHrZix-kWqU hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
matvoc:mat_CH5Br3N2Pb_JIGMU02mJ5xGUdL3GHTEnmu_iQ3- hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
matvoc:mat_CH5Br3N2Pb_R1Jd6-6KvwmRC-E99nyJnM4h2xsk hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
matvoc:mat_CH5Br3N2Pb_RpdhBT3DcpC-Jqt1f3dOqwyrU9Fo hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
matvoc:mat_CH5Br3N2Pb_S5vOenl19vAngeC0zf_44GrFlqfa hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
matvoc:mat_CH5Br3N2Pb_YGZsX22g5rotnlQkOeAypRZ_Owsi hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
matvoc:mat_CH5Br3N2Pb_aNIOR0n5mtu-gHUWKsPBLfkLon8X hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
matvoc:mat_CH5Br3N2Pb_bqeBwCg4_dZkSb4upAc_paVx5hq3 hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
matvoc:mat_CH5Br3N2Pb_eG1G_Cu6_vrQyBPcYn1CSHYVQJY7 hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
matvoc:mat_CH5Br3N2Pb_erekcQqiMmGEs-HYDCJjF0ZpThyP hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
matvoc:mat_CH5Br3N2Pb_f3rZY4yPBsB3OWquv1Lr-h_KjTgE hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
matvoc:mat_CH5Br3N2Pb_ink19SnGrnRvvYnzorUAoFCsw9t5 hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
matvoc:mat_CH5Br3N2Pb_m-0wA23O2c7UDaMOhug7z5won4ay hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
matvoc:mat_CH5Br3N2Pb_rM9JaP2mS0XixoSyT1EAFm1yXw84 hybrid3:has_canonical_formula matvoc:CH5N2PbBr3.\
matvoc:mat_CH5Br3N2Pb_vlvoT-f8k-JWlUdSP_DIB-q92-AM hybrid3:has_canonical_formula matvoc:CH5N2PbBr3. \
matvoc:matvoc:mat_C3H5I3N2Sn_-kwzT9D4XOlu9QV_E-toxSLvKkI0 hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_0BFYoL3UZ_9_U8oL30C02SpYxeEO hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_15EU0Lam-jo378S5m07CRjwWlwkV hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_2Qw8CNkQ6LoaeVaWsUYOOMw4VVZp hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_3l1Nb4Z2FrsN3LwoyRK-9icgMzOY hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_3zCqYVgT2kr36-6__9Ux6mZEtjqi hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_4FlfGF9u-t1YalpkonZxapyCOVFt hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_5VQ_mWi1XhEbnmfkiib7mMKrDz2M hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_61abSmcNoCgtuVeT8PaapCCLFb8i hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_CDTHisCDa7hzfRRjJmB7sR9pWCNj hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_DBCDOwOSyM22N2FAYCX626huwLaB hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_DEIbeUbLXl6IQf_xgqH8c3i644m7 hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_FRFA15wgvkEoTJdBqseK6W-u-ZxD hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_H1g7zUdKv9HPce90uFPepiT1_1s3 hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_HcOSyRL4v34XhDB4rt-hAloMpp-F hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_IT1mKNfLiqhHYZXacMQQi6mXPmnS hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_KngGQHdR2aJnCydwIgLRmIom7gpZ hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_LBcRXcMdBfPBViOK92On183w05uo hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_LIpIx5OmW02t3ql_H-zm2XDgKktV hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_LJ_fUjOAPtS2YuP5uRvzJS1Ir_hJ hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_LVu3UD5XB80o5lnjs14lqQtoi51J hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_Leioul4T1rewyoCxKq6Z4qUE5B5f hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_OY_TI4l_UmSo145pfMskg_EebHNV hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_QeahuXIVSonQD-VA-zZMLMzO8vOH hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_SDN1e0kKeWnQsr0yOnlWmfCIFiCd hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_UugaoSrSW2tRCVk-kUnJzqld3g3z hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_W3G1Yt96doVRrtzs_JsYWgKMAmZQ hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn__tA8jBUhVgKHNNgMNWPTzKjiLQKN hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_bu6sL6mXdko02C7YGyt2_FgcKNID hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_cf8kl9R3XDklstNxrvbC6GbuWSJ9 hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_dRFdRGQ_8R_plANMZcoCLSaNxE8c hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_dWMbbghrpWD36S2gbpVsiF7_EjAf hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_f1TS5wDElni3yt7Ct2uu0z37mY_l hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_fKJISX4nd0KtIsgdW0du3tfmQVZA hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_faRp7iWoDOP2zoqPq-5kNGXjKkZZ hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_g5vAbdYDrfkqStqaT4bvFnMadJG8 hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_g6yrAiEQWGpmrzsANvHHk8zVqJvr hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_gNCgdqafQoKJLz84cPyhlkf3QRA9 hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_go0xeWPMjMIbWtd2Nb-7aOKOhy_D hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_hCscn61g7ToL4DG9-ihDQrlMAKAd hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_j8oIHEXfVsazoLBEMF66OqkNl3nH hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_k1-DN7jRFw7C31Bk0CY3Unbd2yxS hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_kiH4ggDVMuFEdEboCCBWR8Aub7oV hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_lNzTjGmPmLjq4za0Zm18oHazVmzG hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_nccsUxsNoZn6PjoU0QEsQm590RwW hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_oDnjRbzycp7MHbknro1Fo-xT80R3 hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_q-YdP-fbtqafmph0fjX3perahBru hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_rstgTTOPo0PJm8okmKQFVK0iSQ6n hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_sAmgY-5Rd9763rvg6zl1p8Dunrrz hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_tgD2Vx6JGlj00Sf8ZFUfDzmPZL_R hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_xAbPWXRly3x_2yyvSCKczxGC80i4 hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_y_HCaTrH1kC8D9tNU4I5TyZjo3cE hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_z0gBrORRzauIobOkVBRcQFsqn4cj hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_C3H5I3N2Sn_zrO2-S9YTgMobbxCEDlu4ILkBmUc hybrid3:has_canonical_formula matvoc:C3N2H5SnI3. \
matvoc:mat_CH5I3N2Pb_30F6rw0xqsk_iTbjWUusd9bUViAy hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
matvoc:mat_CH5I3N2Pb_4HsmfmOnqQeKCKGIySWvbc861yG1 hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
matvoc:mat_CH5I3N2Pb_89ZsUFCpTjYPleRaJdq1pQQBETng hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
matvoc:mat_CH5I3N2Pb_99qZq9crkqEfevWpa5Wq-_0aw-ol hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
matvoc:mat_CH5I3N2Pb_Df-LkhdYHCr4Wh2kaK6Hvml60ETg hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
matvoc:mat_CH5I3N2Pb_IG91UeXBMYMX1Slz_s77d86zNiib hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
matvoc:mat_CH5I3N2Pb_J7DILGe0QMFnF5aEtRzyICUzUhkT hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
matvoc:mat_CH5I3N2Pb_Lp3IY5Uz2P-UkhpfzNtqMyXr9fse hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
matvoc:mat_CH5I3N2Pb_PX1SX6t9V3-ojacDwChsYX-2De9b hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
matvoc:mat_CH5I3N2Pb_SIRiW0zByBDDjWa1vR-2upBUE6Bq hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
matvoc:mat_CH5I3N2Pb_TOzY0msF1XGarSIhvLcJikOfZ0cy hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
matvoc:mat_CH5I3N2Pb_YgFdR0J3TgFHL6OeySR1xvKsFqfP hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
matvoc:mat_CH5I3N2Pb_Ytsi3qn7Bt_7949ISrpUieVO0DGj hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
matvoc:mat_CH5I3N2Pb_ZMPuXE08HuMh1m-jWJ0b23PSY2N5 hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
matvoc:mat_CH5I3N2Pb_c-5Itp9xhN7rPErrsv8SF3DxAs9K hybrid3:has_canonical_formula matvoc:CH5N2PbI3.\
matvoc:mat_CH5I3N2Pb_fkUjeY3ghtmz6W1qG1dVus7NIXKZ hybrid3:has_canonical_formula matvoc:CH5N2PbI3.\
matvoc:mat_CH5I3N2Pb_lPVA9-NO4O080K77kWYR-zo75gPR hybrid3:has_canonical_formula matvoc:CH5N2PbI3.\
matvoc:mat_CH5I3N2Pb_xsx0EA9YYVdy36s3WbA3e4Lwlpoo hybrid3:has_canonical_formula matvoc:CH5N2PbI3. \
matvoc:mat_CH6Br3NSn_4hX5EWYY3r-WulnTdLm-4GSnztPE hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_77hy58KEL2RJ2uaZdklydIJM0Hk2 hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_7VRqHzhznVh8g8AjBtwI15_zrYo7 hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_8OD2pfYr0z47JJiL8MqjV63vJgYp hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_ANW_pLHkZyrlgBApiqKNJOVa3NjZ hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_CWKU6OPEfPBcZ0jQYSBkDPSMuuoG hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_CxwCHcNz0wDyHWqPAU3CuGG3hFwl hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_DQLz_3Yfvq2Rcb1QhenWI9LaQDab hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_FCRz_CJ_YueraeqWaTKSliRtRTE6 hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_G28dyiEuBIzN8qbWSDAp_93bWHS9 hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_IMrGK-FpLg3QbCvEA9yVCpAZ_Mtg hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_IWA3-HQBsvnwLCURmFFsSQIF2S7_ hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_JN9jZysgacCZL5Tr4WJKAEjNQIK1 hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_JZTohq0HZMLugAB60UFtTqvA3Ujv hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_P_9efogaIN2zRC1PGZxU05Wu1aGt hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_ROQBi8F0GkuORzlQIvR-vlWEfTMA hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_RtE4UGlV5GAx7MSZB6KJ2cq0OKkw hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_UYfoUa3Xl_Ta1KGw5pVhhQzs1vsd hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_UbRX1K1ldQvMBoUGkFcZQWir-LcO hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_Y2B3KbWcahYw8KCigkh62O9-99Lk hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_aFNX9V153WATn17HrbnKVTNL851I hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_aJ8y4l0cPLuS3xjOJrbKH2t-svei hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_f8uARR6qE7teUFqkfuCEHI46ij0i hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_hfE8jy-VsARRojCuNnDgjJW8ugsE hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_joNRMj01YttdqKcwu-LWbzxWRnpP hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_kwWiL0kQoMUMXeczTuoX8lLA_1Lw hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_msGQgvnmZt6r1_a7LzXtwmJ_qAUZ hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_n8lfS0oxZ1qkzvxP6QflTmiwvfBK hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_q2z0f1BK2PbGogFBQ1cDuJOprYdy hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_v0CaYU-JNYnOED74iuONqtWJpN2a hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_vY_Gv_qUvMhTtxcxnNUsL5orKHyI hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_y9183C9W1IvzBhAaUAlzqKQ13Lfz hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_yERi6sdRe3NwW95h2DsgEMOn9c1z hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_yaiDAUgmnoYEJk5vv2X7gGY31YDP hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_CH6Br3NSn_zEHwCsKQwrWFHYr1qtLok0WMzjIi hybrid3:has_canonical_formula matvoc:CH6NSnBr3. matvoc:mat_CH6Br3NSn_zkPJNmtHNB3Ae6gTovZR1oalTCoj hybrid3:has_canonical_formula matvoc:CH6NSnBr3. \
matvoc:mat_C3H8Br3NPb_-DHFm9kuAfH3seAfy9GNwh7kmh6n hybrid3:has_canonical_formula matvoc:C3H8Br3NPb. matvoc:mat_CH6Br3NPb_4FuXctl_VlayNvhk6qkHr12dbpDu hybrid3:has_canonical_formula matvoc:CH6NPbBr3. \
matvoc:mat_C2H8I3NPb_-j6vzE9ZLj34lDgywyCKN2AMr5Az hybrid3:has_canonical_formula matvoc:C2H8NPbI3. } "
    


response = requests.post('http://vm188067-l3s.hosting.uni-hannover.de:7200/repositories/Nomad_hybrid/statements', 
                         headers=headers, data=data)


print(response)








            
            


