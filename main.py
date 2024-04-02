from xml.dom import minidom
import csv
import requests
from datetime import datetime
import xml.etree.ElementTree as ET
import numpy as np
import UKMap
import doctest

def importTownData_csv(filename):
    '''
     import the town data from the latlon csv file
    :param filename: the filename for the towndata file latlon
    :return: The Town dictionary#
    >>> importTownData_csv('latlon.csv')
    {'Abbots Langley': (51.7, -0.41), 'Aberaeron': (52.23, -4.24), 'Aberdare': (51.71, -3.45), 'Aberdyfi': (52.54, -4.04), 'Abergavenny': (51.82, -3.0), 'Abergele': (53.26, -3.59), 'Abertillery': (51.73, -3.14), 'Aberystwyth': (52.38, -4.05), 'Abingdon': (51.66, -1.31), 'Accrington': (53.75, -2.37), 'Addlestone': (51.36, -0.49), 'Alcester': (52.19, -1.85), 'Aldeburgh': (52.15, 1.59), 'Aldershot': (51.25, -0.74), 'Alford': (53.26, 0.18), 'Alfreton': (53.1, -1.37), 'Alnwick': (55.42, -1.73), 'Alresford': (51.08, -1.14), 'Alston': (54.8, -2.41), 'Alton': (51.13, -0.98), 'Altrincham': (53.38, -2.33), 'Ambleside': (54.42, -2.98), 'Amersham': (51.66, -0.59), 'Amlwch': (53.39, -4.37), 'Ammanford': (51.79, -3.95), 'Andover': (51.22, -1.5), 'Appleby-in-Westmorland': (54.57, -2.48), 'Arlesey': (52.01, -0.26), 'Arthog': (52.71, -4.01), 'Arundel': (50.84, -0.57), 'Ascot': (51.4, -0.66), 'Ashbourne': (52.99, -1.71), 'Ashby-de-la-Zouch': (52.74, -1.46), 'Ashford': (51.19, 0.62), 'Ashington': (55.17, -1.56), 'Ashtead': (51.31, -0.3), 'Ashton-under-Lyne': (53.5, -2.07), 'Askam-in-furness': (54.18, -3.2), 'Atherstone': (52.58, -1.55), 'Attleborough': (52.51, 0.99), 'Axbridge': (51.27, -2.85), 'Axminster': (50.78, -3.0), 'Aylesbury': (51.8, -0.84), 'Aylesford': (51.3, 0.46), 'Bacup': (53.7, -2.2), 'Badminton': (51.55, -2.29), 'Bagshot': (51.36, -0.69), 'Bakewell': (53.21, -1.67), 'Bala': (52.9, -3.6), 'Baldock': (52.0, -0.17), 'Bamburgh': (55.6, -1.71), 'Banbury': (52.05, -1.34), 'Bangor': (53.2, -4.11), 'Banstead': (51.32, -0.2), 'Banwell': (51.33, -2.87), 'Bargoed': (51.7, -3.24), 'Barking': (51.53, 0.09), 'Barmouth': (52.72, -4.05), 'Barnard Castle': (54.57, -1.98), 'Barnet': (51.64, -0.17), 'Barnetby': (53.56, -0.39), 'Barnoldswick': (53.91, -2.17), 'Barnsley': (53.54, -1.44), 'Barnstaple': (51.08, -4.04), 'Barrow-in-Furness': (54.11, -3.21), 'Barrow-Upon-Humber': (53.68, -0.35), 'Barry': (51.41, -3.27), 'Barton-Upon-Humber': (53.68, -0.44), 'Basildon': (51.57, 0.46), 'Basingstoke': (51.25, -1.11), 'Bath': (51.38, -2.37), 'Batley': (53.71, -1.64), 'Battle': (50.91, 0.47), 'Beaconsfield': (51.61, -0.63), 'Beaminster': (50.81, -2.75), 'Beaumaris': (53.28, -4.09), 'Beaworthy': (50.8, -4.2), 'Beccles': (52.43, 1.58), 'Beckenham': (51.4, -0.03), 'Beckermet': (54.44, -3.51), 'Bedford': (52.12, -0.47), 'Bedlington': (55.13, -1.58), 'Bedworth': (52.47, -1.47), 'Belford': (55.59, -1.81), 'Belper': (53.02, -1.47), 'Belvedere': (51.48, 0.14), 'Bembridge': (50.68, -1.08), 'Benfleet': (51.56, 0.57), 'Berkeley': (51.69, -2.45), 'Berkhamsted': (51.76, -0.56), 'Betchworth': (51.23, -0.27), 'Betws-y-Coed': (53.05, -3.78), 'Beverley': (53.84, -0.42), 'Bewdley': (52.38, -2.32), 'Bexhill': (50.84, 0.46), 'Bexley': (51.44, 0.14), 'Bexleyheath': (51.45, 0.14), 'Bicester': (51.91, -1.17), 'Bideford': (51.01, -4.24), 'Biggleswade': (52.08, -0.26), 'Billericay': (51.62, 0.42), 'Billingham': (54.61, -1.29), 'Billingshurst': (51.03, -0.48), 'Bilston': (52.55, -2.07), 'Bingley': (53.84, -1.83), 'Birchington': (51.37, 1.3), 'Birkenhead': (53.38, -3.02), 'Birmingham': (52.47, -1.87), 'Bishop Auckland': (54.68, -1.82), 'Bishops Castle': (52.49, -2.98), "Bishop's Stortford": (51.86, 0.19), 'Blackburn': (53.76, -2.46), 'Blackpool': (53.81, -3.03), 'Blackwood': (51.66, -3.19), 'Blaenau Ffestiniog': (52.96, -3.93), 'Blandford Forum': (50.86, -2.18), 'Blaydon': (54.95, -1.71), 'Blyth': (55.12, -1.52), 'Bodmin': (50.48, -4.72), 'Bodorgan': (53.21, -4.38), 'Bognor Regis': (50.78, -0.67), 'Boldon Colliery': (54.95, -1.46), 'Bolton': (53.58, -2.45), 'Boncath': (52.01, -4.59), 'Bootle': (53.48, -2.97), 'Bordon': (51.11, -0.84), 'Borehamwood': (51.65, -0.27), 'Boscastle': (50.68, -4.68), 'Boston': (52.98, -0.03), 'Bourne': (52.77, -0.37), 'Bourne End': (51.57, -0.7), 'Bournemouth': (50.73, -1.86), 'Bow Street': (52.47, -4.02), 'Brackley': (52.03, -1.14), 'Bracknell': (51.41, -0.74), 'Bradford': (53.78, -1.76), 'Bradford-on-Avon': (51.35, -2.26), 'Braintree': (51.89, 0.53), 'Brampton': (54.93, -2.68), 'Brandon': (52.43, 0.58), 'Braunton': (51.11, -4.16), 'Brecon': (51.96, -3.37), 'Brentford': (51.48, -0.3), 'Brentwood': (51.62, 0.31), 'Bridgend': (51.53, -3.59), 'Bridgnorth': (52.51, -2.41), 'Bridgwater': (51.13, -3.0), 'Bridlington': (54.09, -0.18), 'Bridport': (50.73, -2.77), 'Brierley Hill': (52.48, -2.12), 'Brigg': (53.55, -0.5), 'Brighouse': (53.7, -1.78), 'Brighton': (50.84, -0.17), 'Bristol': (51.45, -2.59), 'Brixham': (50.39, -3.52), 'Broadstairs': (51.36, 1.43), 'Broadstone': (50.75, -1.99), 'Broadway': (52.04, -1.87), 'Brockenhurst': (50.81, -1.53), 'Bromley': (51.39, 0.02), 'Bromsgrove': (52.33, -2.05), 'Bromyard': (52.18, -2.52), 'Broseley': (52.61, -2.48), 'Brough': (53.74, -0.62), 'Broughton-in-furness': (54.29, -3.2), 'Broxbourne': (51.74, -0.02), 'Bruton': (51.11, -2.44), 'Brynteg': (53.31, -4.26), 'Buckfastleigh': (50.48, -3.78), 'Buckhurst Hill': (51.62, 0.04), 'Buckingham': (51.98, -0.96), 'Bude': (50.82, -4.53), 'Budleigh Salterton': (50.63, -3.32), 'Builth Wells': (52.14, -3.39), 'Bungay': (52.46, 1.43), 'Buntingford': (51.94, -0.01), 'Bures': (51.97, 0.76), 'Burgess Hill': (50.95, -0.13), 'Burnham-on-Sea': (51.24, -2.99), 'Burnley': (53.79, -2.25), 'Burntwood': (52.68, -1.91), 'Burry Port': (51.68, -4.25), 'Burton upon Trent': (52.8, -1.64), 'Bury': (53.61, -2.3), 'Bury Saint Edmunds': (52.25, 0.71), 'Bushey': (51.64, -0.36), 'Buxton': (53.24, -1.87), 'Caernarfon': (53.09, -4.24), 'Caerphilly': (51.58, -3.21), 'Caersws': (52.51, -3.46), 'Caldicot': (51.59, -2.77), 'Callington': (50.51, -4.3), 'Calne': (51.43, -1.99), 'Camberley': (51.32, -0.74), 'Camborne': (50.21, -5.29), 'Cambridge': (52.2, 0.13), 'Camelford': (50.63, -4.66), 'Cannock': (52.69, -2.0), 'Canterbury': (51.26, 1.11), 'Canvey Island': (51.52, 0.59), 'Cardiff': (51.5, -3.19), 'Cardigan': (52.08, -4.62), 'Carlisle': (54.89, -2.92), 'Carmarthen': (51.86, -4.3), 'Carnforth': (54.16, -2.7), 'Carshalton': (51.36, -0.16), 'Carterton': (51.76, -1.59), 'Castle Cary': (51.08, -2.51), 'Castleford': (53.72, -1.34), 'Caterham': (51.28, -0.08), 'Catterick Garrison': (54.37, -1.7), 'Cemaes Bay': (53.41, -4.45), 'Chalfont Saint Giles': (51.64, -0.57), 'Chard': (50.87, -2.96), 'Chatham': (51.36, 0.53), 'Chathill': (55.53, -1.69), 'Chatteris': (52.45, 0.05), 'Cheadle': (53.38, -2.2), 'Cheddar': (51.27, -2.77), 'Chelmsford': (51.73, 0.5), 'Cheltenham': (51.89, -2.03), 'Chepstow': (51.65, -2.68), 'Chertsey': (51.38, -0.51), 'Chesham': (51.71, -0.6), 'Chessington': (51.36, -0.3), 'Chester': (53.18, -2.88), 'Chesterfield': (53.22, -1.39), 'Chester Le Street': (54.86, -1.58), 'Chichester': (50.82, -0.79), 'Chigwell': (51.61, 0.08), 'Chinnor': (51.7, -0.91), 'Chippenham': (51.47, -2.13), 'Chipping Campden': (52.06, -1.76), 'Chipping Norton': (51.91, -1.52), 'Chislehurst': (51.41, 0.07), 'Choppington': (55.16, -1.59), 'Chorley': (53.65, -2.62), 'Christchurch': (50.74, -1.75), 'Chulmleigh': (50.9, -3.88), 'Church Stretton': (52.53, -2.79), 'Cinderford': (51.81, -2.47), 'Cirencester': (51.71, -1.89), 'Clacton-on-Sea': (51.8, 1.14), 'Clarbeston Road': (51.87, -4.85), 'Cleator': (54.51, -3.49), 'Cleator Moor': (54.52, -3.51), 'Cleckheaton': (53.72, -1.71), 'Cleethorpes': (53.55, -0.03), 'Clevedon': (51.43, -2.84), 'Clitheroe': (53.87, -2.38), 'Clynderwen': (51.88, -4.74), 'Coalville': (52.71, -1.36), 'Cobham': (51.32, -0.4), 'Cockermouth': (54.66, -3.36), 'Colchester': (51.88, 0.88), 'Coleford': (51.79, -2.61), 'Colne': (53.85, -2.16), 'Colwyn Bay': (53.28, -3.73), 'Colyton': (50.73, -3.08), 'Congleton': (53.16, -2.21), 'Coniston': (54.36, -3.07), 'Consett': (54.85, -1.84), 'Conwy': (53.27, -3.82), 'Corbridge': (54.97, -2.01), 'Corby': (52.49, -0.7), 'Corsham': (51.42, -2.21), 'Corwen': (52.99, -3.4), 'Cottingham': (53.78, -0.46), 'Coulsdon': (51.31, -0.13), 'Coventry': (52.41, -1.52), 'Cowbridge': (51.46, -3.45), 'Cowes': (50.75, -1.3), 'Cradley Heath': (52.47, -2.06), 'Cramlington': (55.08, -1.58), 'Cranbrook': (51.06, 0.53), 'Cranleigh': (51.14, -0.48), 'Craven Arms': (52.42, -2.88), 'Crawley': (51.11, -0.17), 'Crediton': (50.81, -3.7), 'Crewe': (53.09, -2.4), 'Crewkerne': (50.88, -2.78), 'Criccieth': (52.92, -4.24), 'Crickhowell': (51.86, -3.14), 'Cromer': (52.92, 1.3), 'Crook': (54.71, -1.72), 'Crowborough': (51.05, 0.17), 'Crowthorne': (51.37, -0.8), 'Croydon': (51.37, -0.07), 'Crymych': (51.99, -4.7), 'Cullompton': (50.87, -3.33), 'Cwmbran': (51.65, -3.02), 'Dagenham': (51.54, 0.14), 'Dalton-in-Furness': (54.15, -3.17), 'Darlington': (54.53, -1.57), 'Dartford': (51.42, 0.22), 'Dartmouth': (50.34, -3.58), 'Darwen': (53.69, -2.46), 'Daventry': (52.24, -1.17), 'Dawlish': (50.59, -3.47), 'Deal': (51.21, 1.38), 'Deeside': (53.2, -3.04), 'Delabole': (50.62, -4.73), 'Denbigh': (53.18, -3.43), 'Derby': (52.89, -1.46), 'Dereham': (52.7, 0.95), 'Devizes': (51.33, -1.98), 'Dewsbury': (53.69, -1.63), 'Didcot': (51.59, -1.24), 'Diss': (52.37, 1.05), 'Dolgellau': (52.75, -3.87), 'Dolwyddelan': (53.05, -3.87), 'Doncaster': (53.52, -1.07), 'Dorchester': (50.73, -2.45), 'Dorking': (51.2, -0.34), 'Dover': (51.14, 1.29), 'Downham Market': (52.58, 0.37), 'Driffield': (54.0, -0.41), 'Droitwich': (52.26, -2.15), 'Dronfield': (53.29, -1.47), 'Drybrook': (51.85, -2.51), 'Dudley': (52.51, -2.1), 'Dukinfield': (53.47, -2.08), 'Dulas': (53.36, -4.28), 'Dulverton': (51.04, -3.54), 'Dunmow': (51.87, 0.36), 'Dunstable': (51.88, -0.52), 'Durham': (54.77, -1.56), 'Dursley': (51.68, -2.35), 'Dyffryn Ardudwy': (52.79, -4.09), 'East Boldon': (54.94, -1.43), 'Eastbourne': (50.78, 0.28), 'East Cowes': (50.75, -1.28), 'East Grinstead': (51.12, -0.01), 'Eastleigh': (50.97, -1.35), 'Ebbw Vale': (51.78, -3.19), 'Edenbridge': (51.19, 0.07), 'Edgware': (51.61, -0.27), 'Egham': (51.42, -0.55), 'Egremont': (54.48, -3.53), 'Elland': (53.68, -1.83), 'Ellesmere': (52.9, -2.89), 'Ellesmere Port': (53.27, -2.92), 'Ely': (52.38, 0.27), 'Emsworth': (50.85, -0.92), 'Enfield': (51.65, -0.06), 'Epping': (51.7, 0.12), 'Epsom': (51.33, -0.25), 'Erith': (51.48, 0.16), 'Esher': (51.36, -0.35), 'Etchingham': (51.0, 0.4), 'Evesham': (52.09, -1.92), 'Exeter': (50.71, -3.5), 'Exmouth': (50.62, -3.4), 'Eye': (52.33, 1.18), 'Fairbourne': (52.69, -4.03), 'Fakenham': (52.84, 0.85), 'Falmouth': (50.14, -5.08), 'Fareham': (50.85, -1.18), 'Faringdon': (51.64, -1.56), 'Farnborough': (51.29, -0.76), 'Farnham': (51.2, -0.79), 'Faversham': (51.3, 0.89), 'Felixstowe': (51.97, 1.33), 'Feltham': (51.44, -0.41), 'Ferndale': (51.65, -3.44), 'Ferndown': (50.8, -1.88), 'Ferryhill': (54.68, -1.54), 'Ferryside': (51.75, -4.28), 'Filey': (54.19, -0.29), 'Fishguard': (51.98, -4.96), 'Fleet': (51.27, -0.83), 'Fleetwood': (53.91, -3.02), 'Flint': (53.25, -3.14), 'Folkestone': (51.09, 1.16), 'Fordingbridge': (50.93, -1.8), 'Forest Row': (51.09, 0.03), 'Fowey': (50.33, -4.63), 'Freshwater': (50.68, -1.52), 'Frinton-on-Sea': (51.83, 1.23), 'Frizington': (54.54, -3.48), 'Frodsham': (53.27, -2.72), 'Frome': (51.23, -2.32), 'Gaerwen': (53.21, -4.27), 'Gainsborough': (53.41, -0.7), 'Garndolbenmaen': (52.97, -4.23), 'Gateshead': (54.94, -1.59), 'Gerrards Cross': (51.59, -0.55), 'Gillingham': (51.25, -0.38), 'Glastonbury': (51.14, -2.7), 'Glogue': (51.95, -4.6), 'Glossop': (53.44, -1.96), 'Gloucester': (51.87, -2.23), 'Godalming': (51.16, -0.62), 'Godstone': (51.23, -0.06), 'Goodwick': (52.0, -5.01), 'Goole': (53.7, -0.93), 'Gosport': (50.79, -1.14), 'Grange-over-Sands': (54.2, -2.92), 'Grantham': (52.89, -0.62), 'Gravesend': (51.41, 0.36), 'Grays': (51.48, 0.32), 'Great Missenden': (51.7, -0.71), 'Great Yarmouth': (52.62, 1.69), 'Greenford': (51.53, -0.34), 'Greenhithe': (51.44, 0.28), 'Grimsby': (53.55, -0.1), 'Guildford': (51.23, -0.56), 'Guisborough': (54.53, -1.06), 'Gunnislake': (50.51, -4.21), 'Hailsham': (50.87, 0.26), 'Halesowen': (52.45, -2.04), 'Halesworth': (52.34, 1.49), 'Halifax': (53.71, -1.87), 'Halstead': (51.96, 0.61), 'Haltwhistle': (54.96, -2.45), 'Hampton': (51.42, -0.36), 'Harlech': (52.85, -4.1), 'Harleston': (52.4, 1.32), 'Harlow': (51.76, 0.1), 'Harpenden': (51.81, -0.35), 'Harrogate': (54.0, -1.55), 'Harrow': (51.58, -0.33), 'Hartfield': (51.09, 0.1), 'Hartlepool': (54.69, -1.23), 'Harwich': (51.93, 1.25), 'Haslemere': (51.08, -0.71), 'Hassocks': (50.92, -0.15), 'Hastings': (50.87, 0.59), 'Hatfield': (51.75, -0.21), 'Havant': (50.86, -0.98), 'Haverfordwest': (51.82, -5.01), 'Haverhill': (52.08, 0.44), 'Hayes': (51.51, -0.41), 'Hayle': (50.18, -5.4), 'Hayling Island': (50.79, -0.97), 'Haywards Heath': (51.01, -0.1), 'Heanor': (53.01, -1.35), 'Heathfield': (50.95, 0.26), 'Hebburn': (54.97, -1.51), 'Hebden Bridge': (53.73, -2.0), 'Heckmondwike': (53.71, -1.66), 'Helston': (50.07, -5.22), 'Hemel Hempstead': (51.75, -0.47), 'Henfield': (50.92, -0.26), 'Hengoed': (51.65, -3.23), 'Henley-in-Arden': (52.28, -1.77), 'Henley-on-Thames': (51.54, -0.92), 'Henlow': (52.01, -0.29), 'Hereford': (52.06, -2.82), 'Herne Bay': (51.36, 1.13), 'Hertford': (51.79, -0.07), 'Hessle': (53.72, -0.43), 'Hexham': (55.01, -2.2), 'Heywood': (53.59, -2.22), 'Highbridge': (51.22, -2.95), 'High Peak': (53.34, -1.96), 'High Wycombe': (51.63, -0.75), 'Hinckley': (52.53, -1.36), 'Hindhead': (51.11, -0.74), 'Hinton Saint George': (50.9, -2.83), 'Hitchin': (51.94, -0.27), 'Hockley': (51.6, 0.65), 'Hoddesdon': (51.76, -0.01), 'Holmfirth': (53.58, -1.79), 'Holmrook': (54.38, -3.38), 'Holsworthy': (50.82, -4.36), 'Holt': (52.92, 1.08), 'Holyhead': (53.3, -4.56), 'Holywell': (53.28, -3.24), 'Honiton': (50.81, -3.18), 'Hook': (51.27, -0.94), 'Hope Valley': (53.31, -1.67), 'Horley': (51.17, -0.16), 'Horncastle': (53.21, -0.11), 'Hornchurch': (51.56, 0.21), 'Hornsea': (53.9, -0.16), 'Horsham': (51.05, -0.33), 'Houghton Le Spring': (54.84, -1.47), 'Hounslow': (51.47, -0.39), 'Hove': (50.83, -0.17), 'Huddersfield': (53.63, -1.78), 'Hull': (53.76, -0.32), 'Hungerford': (51.44, -1.48), 'Hunstanton': (52.93, 0.5), 'Huntingdon': (52.38, -0.15), 'Hyde': (53.45, -2.05), 'Hythe': (51.07, 1.07), 'Ilford': (51.57, 0.07), 'Ilfracombe': (51.19, -4.1), 'Ilkeston': (52.97, -1.32), 'Ilkley': (53.92, -1.8), 'Ilminster': (50.93, -2.91), 'Immingham': (53.62, -0.22), 'Ingatestone': (51.67, 0.39), 'Ipswich': (52.05, 1.14), 'Isles Of Scilly': (49.94, -6.31), 'Isleworth': (51.47, -0.33), 'Iver': (51.52, -0.51), 'Ivybridge': (50.38, -3.91), 'Jarrow': (54.96, -1.48), 'Keighley': (53.86, -1.93), 'Kendal': (54.32, -2.75), 'Kenilworth': (52.35, -1.54), 'Keswick': (54.6, -3.13), 'Kettering': (52.4, -0.7), 'Kidderminster': (52.38, -2.31), 'Kidlington': (51.82, -1.28), 'Kilgetty': (51.72, -4.76), 'Kingsbridge': (50.28, -3.78), 'Kings Langley': (51.7, -0.45), "King's Lynn": (52.74, 0.48), 'Kingston Upon Thames': (51.41, -0.29), 'Kingswinford': (52.49, -2.16), 'Kington': (52.19, -3.02), 'Kirkby-in-Furness': (54.23, -3.17), 'Kirkby Stephen': (54.47, -2.35), 'Knaresborough': (54.01, -1.45), 'Knebworth': (51.86, -0.18), 'Knighton': (52.35, -3.08), 'Knottingley': (53.71, -1.25), 'Knutsford': (53.3, -2.37), 'Lampeter': (52.14, -4.11), 'Lancaster': (54.05, -2.73), 'Lancing': (50.83, -0.32), 'Langport': (51.03, -2.82), 'Launceston': (50.63, -4.39), 'Leamington Spa': (52.27, -1.51), 'Leatherhead': (51.28, -0.37), 'Ledbury': (52.04, -2.44), 'Leeds': (53.81, -1.55), 'Leek': (53.1, -2.01), 'Lee-on-the-solent': (50.81, -1.17), 'Leicester': (52.62, -1.14), 'Leigh': (53.49, -2.51), 'Leigh-on-Sea': (51.55, 0.65), 'Leighton Buzzard': (51.9, -0.66), 'Leiston': (52.2, 1.58), 'Leominster': (52.23, -2.77), 'Letchworth': (51.97, -0.22), 'Lewes': (50.89, 0.03), 'Leyburn': (54.29, -1.78), 'Leyland': (53.69, -2.71), 'Lichfield': (52.67, -1.81), 'Lifton': (50.64, -4.26), 'Lightwater': (51.34, -0.67), 'Lincoln': (53.21, -0.5), 'Lingfield': (51.17, -0.01), 'Liphook': (51.07, -0.8), 'Liskeard': (50.46, -4.46), 'Liss': (51.04, -0.89), 'Littleborough': (53.64, -2.1), 'Littlehampton': (50.81, -0.51), 'Little Walsingham': (52.89, 0.86), 'Liverpool': (53.43, -2.93), 'Liversedge': (53.7, -1.69), 'Llanarth': (52.19, -4.29), 'Llanbedr': (52.82, -4.09), 'Llanbedrgoch': (53.3, -4.23), 'Llanbrynmair': (52.57, -3.61), 'Llandeilo': (51.95, -3.94), 'Llandovery': (52.01, -3.78), 'Llandrindod Wells': (52.26, -3.36), 'Llandudno': (53.31, -3.81), 'Llandysul': (52.08, -4.37), 'Llanelli': (51.72, -4.13), 'Llanerchymedd': (53.32, -4.36), 'Llanfairfechan': (53.25, -3.98), 'Llanfairpwllgwyngyll': (53.19, -4.26), 'Llanfyrnach': (51.97, -4.56), 'Llangammarch Wells': (52.11, -3.55), 'Llangefni': (53.26, -4.31), 'Llangollen': (52.95, -3.15), 'Llanidloes': (52.44, -3.54), 'Llanrwst': (53.13, -3.78), 'Llantwit Major': (51.4, -3.48), 'Llanwrtyd Wells': (52.12, -3.61), 'Llanybydder': (52.08, -4.17), 'Llwyngwril': (52.66, -4.08), 'London': (51.51, -0.11), 'Longfield': (51.38, 0.31), 'Looe': (50.35, -4.47), 'Lostwithiel': (50.4, -4.65), 'Loughborough': (52.76, -1.2), 'Loughton': (51.64, 0.06), 'Louth': (53.37, 0.02), 'Lowestoft': (52.47, 1.72), 'Ludlow': (52.36, -2.69), 'Luton': (51.89, -0.43), 'Lutterworth': (52.46, -1.17), 'Lydney': (51.73, -2.55), 'Lyme Regis': (50.72, -2.94), 'Lymington': (50.75, -1.56), 'Lymm': (53.38, -2.46), 'Lyndhurst': (50.88, -1.58), 'Lynton': (51.22, -3.82), 'Lytham Saint Annes': (53.75, -3.0), 'Mablethorpe': (53.32, 0.26), 'Macclesfield': (53.26, -2.13), 'Machynlleth': (52.61, -3.81), 'Maesteg': (51.61, -3.65), 'Maidenhead': (51.52, -0.72), 'Maidstone': (51.25, 0.52), 'Maldon': (51.74, 0.7), 'Malmesbury': (51.59, -2.09), 'Malpas': (53.03, -2.76), 'Malton': (54.13, -0.75), 'Malvern': (52.1, -2.33), 'Manchester': (53.47, -2.27), 'Manningtree': (51.94, 1.07), 'Mansfield': (53.16, -1.16), 'Marazion': (50.12, -5.46), 'March': (52.53, 0.08), 'Margate': (51.38, 1.39), 'Marianglas': (53.33, -4.24), 'Market Drayton': (52.89, -2.46), 'Market Harborough': (52.48, -0.89), 'Market Rasen': (53.43, -0.33), 'Marlborough': (51.4, -1.68), 'Marlow': (51.57, -0.77), 'Martock': (50.97, -2.77), 'Maryport': (54.71, -3.48), 'Matlock': (53.12, -1.56), 'Mayfield': (51.02, 0.25), 'Meifod': (52.75, -3.18), 'Melksham': (51.37, -2.13), 'Melton Constable': (52.85, 1.05), 'Melton Mowbray': (52.77, -0.89), 'Menai Bridge': (53.23, -4.15), 'Merriott': (50.9, -2.79), 'Merthyr Tydfil': (51.75, -3.37), 'Mexborough': (53.49, -1.29), 'Middlesbrough': (54.54, -1.2), 'Middlewich': (53.18, -2.44), 'Midhurst': (50.98, -0.74), 'Milford Haven': (51.71, -5.01), 'Millom': (54.25, -3.32), 'Milnthorpe': (54.22, -2.77), 'Milton Keynes': (52.03, -0.76), 'Minehead': (51.18, -3.51), 'Mirfield': (53.68, -1.69), 'Mitcham': (51.4, -0.15), 'Moelfre': (53.35, -4.24), 'Mold': (53.16, -3.13), 'Monmouth': (51.8, -2.72), 'Montacute': (50.95, -2.71), 'Montgomery': (52.55, -3.13), 'Moor Row': (54.51, -3.54), 'Morden': (51.39, -0.19), 'Morecambe': (54.06, -2.86), 'Moreton-in-Marsh': (51.98, -1.7), 'Morpeth': (55.25, -1.71), 'Mountain Ash': (51.66, -3.36), 'Much Hadham': (51.84, 0.07), 'Much Wenlock': (52.57, -2.58), 'Nantwich': (53.06, -2.52), 'Narberth': (51.78, -4.73), 'Neath': (51.67, -3.77), 'Nelson': (53.83, -2.21), 'Neston': (53.28, -3.04), 'Newark': (53.12, -0.85), 'Newbiggin-by-the-Sea': (55.18, -1.51), 'Newbury': (51.39, -1.33), 'Newcastle Emlyn': (52.04, -4.47), 'Newcastle-under-Lyme': (53.01, -2.23), 'Newcastle Upon Tyne': (55.0, -1.68), 'Newent': (51.94, -2.41), 'Newhaven': (50.79, 0.05), 'New Malden': (51.39, -0.25), 'Newmarket': (52.23, 0.42), 'New Milton': (50.75, -1.65), 'Newport': (51.68, -2.95), 'Newport Pagnell': (52.08, -0.72), 'Newquay': (50.4, -5.05), 'New Quay': (52.2, -4.35), 'New Romney': (50.98, 0.95), 'Newton Abbot': (50.56, -3.66), 'Newton Aycliffe': (54.61, -1.57), 'Newton-le-Willows': (53.45, -2.63), 'Newtown': (52.52, -3.31), 'New Tredegar': (51.72, -3.23), 'Normanton': (53.7, -1.41), 'Northallerton': (54.35, -1.43), 'Northampton': (52.25, -0.9), 'North Ferriby': (53.72, -0.5), 'Northolt': (51.54, -0.37), 'North Shields': (55.02, -1.45), 'North Walsham': (52.82, 1.4), 'Northwich': (53.25, -2.53), 'Northwood': (51.61, -0.42), 'Norwich': (52.64, 1.27), 'Nottingham': (52.97, -1.15), 'Nuneaton': (52.55, -1.45), 'Oakham': (52.65, -0.7), 'Okehampton': (50.75, -4.01), 'Oldbury': (52.48, -2.01), 'Oldham': (53.54, -2.09), 'Olney': (52.15, -0.69), 'Ongar': (51.72, 0.24), 'Ormskirk': (53.58, -2.87), 'Orpington': (51.38, 0.1), 'Ossett': (53.68, -1.57), 'Oswestry': (52.84, -3.07), 'Otley': (53.91, -1.67), 'Ottery Saint Mary': (50.74, -3.28), 'Oxford': (51.77, -1.23), 'Oxted': (51.25, 0.0), 'Padstow': (50.53, -4.96), 'Paignton': (50.43, -3.57), 'Par': (50.35, -4.71), 'Peacehaven': (50.79, 0.0), 'Pembroke': (51.66, -4.92), 'Pembroke Dock': (51.69, -4.93), 'Penarth': (51.43, -3.18), 'Pencader': (52.02, -4.24), 'Penmaenmawr': (53.27, -3.91), 'Penrhyndeudraeth': (52.93, -4.07), 'Penrith': (54.63, -2.71), 'Penryn': (50.16, -5.11), 'Pentraeth': (53.28, -4.21), 'Pentre': (51.64, -3.48), 'Penysarn': (53.38, -4.31), 'Penzance': (50.11, -5.55), 'Perranporth': (50.34, -5.15), 'Pershore': (52.11, -2.06), 'Peterborough': (52.57, -0.28), 'Peterlee': (54.76, -1.33), 'Petersfield': (51.0, -0.94), 'Petworth': (50.99, -0.63), 'Pevensey': (50.81, 0.33), 'Pewsey': (51.32, -1.78), 'Pickering': (54.25, -0.76), 'Pinner': (51.59, -0.38), 'Plymouth': (50.38, -4.11), 'Polegate': (50.82, 0.22), 'Pontefract': (53.65, -1.32), 'Pontyclun': (51.53, -3.39), 'Pontypool': (51.71, -3.04), 'Pontypridd': (51.58, -3.33), 'Poole': (50.72, -1.96), 'Porth': (51.6, -3.42), 'Porthcawl': (51.48, -3.69), 'Porthmadog': (52.92, -4.13), 'Port Isaac': (50.58, -4.82), 'Portland': (50.54, -2.44), 'Portsmouth': (50.81, -1.06), 'Port Talbot': (51.6, -3.75), 'Potters Bar': (51.69, -0.17), 'Poulton-Le-Fylde': (53.86, -2.98), 'Prenton': (53.38, -3.05), 'Prescot': (53.42, -2.79), 'Prestatyn': (53.33, -3.4), 'Presteigne': (52.26, -3.04), 'Preston': (53.77, -2.72), 'Princes Risborough': (51.71, -0.83), 'Prudhoe': (54.96, -1.85), 'Pudsey': (53.8, -1.66), 'Pulborough': (50.93, -0.47), 'Purfleet': (51.48, 0.24), 'Purley': (51.33, -0.11), 'Pwllheli': (52.88, -4.49), 'Queenborough': (51.41, 0.74), 'Radlett': (51.68, -0.3), 'Radstock': (51.27, -2.47), 'Rainham': (51.52, 0.19), 'Ramsgate': (51.34, 1.39), 'Ravenglass': (54.35, -3.39), 'Rayleigh': (51.58, 0.6), 'Reading': (51.45, -0.98), 'Redcar': (54.59, -1.04), 'Redditch': (52.28, -1.94), 'Redhill': (51.23, -0.15), 'Redruth': (50.23, -5.22), 'Reigate': (51.23, -0.2), 'Retford': (53.32, -0.92), 'Rhayader': (52.3, -3.5), 'Rhosgoch': (53.38, -4.4), 'Rhosneigr': (53.22, -4.51), 'Rhyl': (53.31, -3.47), 'Richmond': (52.94, -1.04), 'Rickmansworth': (51.64, -0.48), 'Riding Mill': (54.94, -1.97), 'Ringwood': (50.84, -1.78), 'Ripley': (53.04, -1.4), 'Ripon': (54.15, -1.56), 'Robertsbridge': (50.98, 0.49), 'Rochdale': (53.61, -2.15), 'Rochester': (51.4, 0.51), 'Rochford': (51.59, 0.71), 'Romford': (51.59, 0.17), 'Romney Marsh': (50.99, 0.93), 'Romsey': (50.99, -1.5), 'Rossendale': (53.7, -2.29), 'Ross-on-Wye': (51.9, -2.58), 'Rotherham': (53.45, -1.33), 'Rowlands Gill': (54.92, -1.75), 'Rowley Regis': (52.48, -2.04), 'Royal Tunbridge Wells': (51.13, 0.26), 'Royston': (52.06, -0.01), 'Rugby': (52.36, -1.28), 'Rugeley': (52.75, -1.91), 'Ruislip': (51.57, -0.4), 'Runcorn': (53.33, -2.7), 'Rushden': (52.29, -0.59), 'Ruthin': (53.1, -3.31), 'Ryde': (50.72, -1.16), 'Rye': (50.96, 0.68), 'Ryton': (54.96, -1.77), 'Saffron Walden': (52.02, 0.23), 'Saint Agnes': (50.3, -5.19), 'Saint Albans': (51.75, -0.33), 'Saint Asaph': (53.25, -3.43), 'Saint Austell': (50.34, -4.79), 'Saint Bees': (54.49, -3.59), 'Saint Columb': (50.41, -4.93), 'Saint Helens': (53.45, -2.72), 'Saint Ives': (51.27, -2.77), 'Saint Leonards-on-sea': (50.86, 0.55), 'Saint Neots': (52.24, -0.25), 'Salcombe': (50.23, -3.77), 'Sale': (53.42, -2.32), 'Salford': (53.48, -2.27), 'Salisbury': (51.08, -1.83), 'Saltash': (50.41, -4.24), 'Saltburn-by-the-Sea': (54.55, -0.91), 'Sandbach': (53.14, -2.36), 'Sandhurst': (51.34, -0.78), 'Sandown': (50.65, -1.16), 'Sandringham': (52.82, 0.51), 'Sandwich': (51.26, 1.33), 'Sandy': (52.13, -0.24), 'Saundersfoot': (51.71, -4.7), 'Sawbridgeworth': (51.81, 0.14), 'Saxmundham': (52.23, 1.5), 'Scarborough': (54.27, -0.43), 'Scunthorpe': (53.58, -0.66), 'Seaford': (50.77, 0.11), 'Seaham': (54.83, -1.36), 'Seahouses': (55.57, -1.65), 'Seascale': (54.41, -3.46), 'Seaton': (50.7, -3.08), 'Seaview': (50.71, -1.11), 'Sedbergh': (54.31, -2.49), 'Selby': (53.78, -1.05), 'Settle': (54.07, -2.27), 'Sevenoaks': (51.29, 0.2), 'Shaftesbury': (51.0, -2.18), 'Shanklin': (50.63, -1.17), 'Sheerness': (51.42, 0.8), 'Sheffield': (53.37, -1.44), 'Shefford': (52.03, -0.33), 'Shepperton': (51.39, -0.44), 'Shepton Mallet': (51.17, -2.53), 'Sherborne': (50.94, -2.51), 'Sheringham': (52.93, 1.21), 'Shifnal': (52.66, -2.36), 'Shildon': (54.63, -1.64), 'Shipley': (53.84, -1.77), 'Shipston-on-Stour': (52.06, -1.62), 'Shoreham-by-Sea': (50.83, -0.26), 'Shrewsbury': (52.71, -2.76), 'Sidcup': (51.43, 0.11), 'Sidmouth': (50.69, -3.24), 'Sittingbourne': (51.34, 0.72), 'Skegness': (53.16, 0.3), 'Skelmersdale': (53.55, -2.76), 'Skipton-on-Swale': (53.99, -2.05), 'Sleaford': (52.98, -0.39), 'Slough': (51.51, -0.59), 'Smethwick': (52.48, -1.96), 'Snodland': (51.32, 0.44), 'Solihull': (52.39, -1.78), 'Somerton': (51.06, -2.7), 'Southall': (51.5, -0.37), 'Southam': (52.23, -1.38), 'Southampton': (50.91, -1.37), 'South Brent': (50.42, -3.81), 'South Croydon': (51.35, -0.08), 'Southend-on-Sea': (51.54, 0.74), 'Southminster': (51.66, 0.83), 'South Molton': (51.01, -3.79), 'South Ockendon': (51.5, 0.27), 'South Petherton': (50.94, -2.81), 'Southport': (53.64, -2.98), 'Southsea': (50.78, -1.07), 'South Shields': (54.98, -1.42), 'Southwell': (53.07, -0.95), 'Southwold': (52.33, 1.67), 'Sowerby Bridge': (53.69, -1.92), 'Spalding': (52.79, -0.07), 'Spennymoor': (54.69, -1.6), 'Spilsby': (53.17, 0.09), 'Stafford': (52.79, -2.15), 'Staines': (51.44, -0.5), 'Stalybridge': (53.48, -2.04), 'Stamford': (52.65, -0.48), 'Stanford-le-Hope': (51.52, 0.44), 'Stanley': (54.86, -1.7), 'Stanmore': (51.61, -0.3), 'Stansted': (51.89, 0.2), 'Stevenage': (51.9, -0.17), 'Steyning': (50.89, -0.32), 'Stockbridge': (51.11, -1.5), 'Stockport': (53.39, -2.13), 'Stocksfield': (54.94, -1.9), 'Stockton-on-Tees': (54.56, -1.34), 'Stoke-on-trent': (53.02, -2.13), 'Stoke-sub-hamdon': (50.94, -2.75), 'Stone': (52.9, -2.14), 'Stonehouse': (51.74, -2.28), 'Stourbridge': (52.45, -2.16), 'Stourport-on-Severn': (52.33, -2.28), 'Stowmarket': (52.2, 1.03), 'Stratford-Upon-Avon': (52.18, -1.71), 'Street': (51.12, -2.74), 'Stroud': (51.73, -2.2), 'Studley': (52.27, -1.89), 'Sturminster Newton': (50.93, -2.33), 'Sudbury': (52.05, 0.72), 'Sunbury-on-thames': (51.41, -0.41), 'Sunderland': (54.9, -1.39), 'Surbiton': (51.39, -0.29), 'Sutton': (51.36, -0.2), 'Sutton Coldfield': (52.56, -1.82), 'Swadlincote': (52.75, -1.55), 'Swaffham': (52.64, 0.69), 'Swanage': (50.61, -1.97), 'Swanley': (51.39, 0.17), 'Swanscombe': (51.44, 0.3), 'Swansea': (51.66, -3.93), 'Swindon': (51.57, -1.78), 'Tadcaster': (53.87, -1.25), 'Tadley': (51.35, -1.11), 'Tadworth': (51.28, -0.23), 'Talsarnau': (52.9, -4.06), 'Talybont': (52.77, -4.09), 'Tamworth': (52.62, -1.67), 'Tarporley': (53.16, -2.66), 'Taunton': (51.02, -3.12), 'Tavistock': (50.55, -4.15), 'Teddington': (51.42, -0.33), 'Teignmouth': (50.55, -3.5), 'Telford': (52.68, -2.48), 'Templecombe': (50.99, -2.41), 'Tenbury Wells': (52.3, -2.56), 'Tenby': (51.67, -4.73), 'Tenterden': (51.06, 0.69), 'Tetbury': (51.64, -2.17), 'Tewkesbury': (52.0, -2.13), 'Thame': (51.73, -0.98), 'Thames Ditton': (51.38, -0.32), 'Thatcham': (51.41, -1.24), 'Thetford': (52.5, 0.72), 'Thirsk': (54.22, -1.35), 'Thornton-cleveleys': (53.87, -3.02), 'Thornton Heath': (51.39, -0.1), 'Tidworth': (51.23, -1.66), 'Tilbury': (51.46, 0.37), 'Tintagel': (50.65, -4.74), 'Tipton': (52.53, -2.05), 'Tiverton': (50.92, -3.49), 'Todmorden': (53.71, -2.09), 'Tonbridge': (51.19, 0.31), 'Tonypandy': (51.62, -3.45), 'Torpoint': (50.36, -4.23), 'Torquay': (50.47, -3.53), 'Torrington': (50.94, -4.15), 'Totland Bay': (50.68, -1.53), 'Totnes': (50.41, -3.69), 'Towcester': (52.12, -0.99), 'Tredegar': (51.77, -3.25), 'Trefriw': (53.14, -3.82), 'Treharris': (51.66, -3.3), 'Treorchy': (51.66, -3.52), 'Trimdon Station': (54.71, -1.41), 'Tring': (51.79, -0.66), 'Trowbridge': (51.31, -2.2), 'Truro': (50.25, -5.06), 'Twickenham': (51.45, -0.33), 'Ty Croes': (53.21, -4.47), 'Tyn-Y-Gongl': (53.31, -4.23), 'Tywyn': (52.6, -4.06), 'Uckfield': (50.98, 0.1), 'Ulceby': (53.61, -0.33), 'Ulverston': (54.2, -3.08), 'Umberleigh': (50.97, -3.95), 'Upminster': (51.55, 0.26), 'Usk': (51.72, -2.88), 'Uttoxeter': (52.9, -1.86), 'Uxbridge': (51.54, -0.47), 'Ventnor': (50.6, -1.24), 'Verwood': (50.87, -1.87), 'Virginia Water': (51.4, -0.57), 'Wadebridge': (50.52, -4.87), 'Wadhurst': (51.06, 0.36), 'Wakefield': (53.68, -1.51), 'Wallasey': (53.41, -3.04), 'Wallingford': (51.6, -1.12), 'Wallington': (51.36, -0.14), 'Wallsend': (55.0, -1.51), 'Walsall': (52.6, -1.96), 'Waltham Abbey': (51.69, 0.01), 'Waltham Cross': (51.7, -0.04), 'Walton-on-Thames': (51.37, -0.4), 'Walton On The Naze': (51.85, 1.26), 'Wantage': (51.59, -1.42), 'Ware': (51.84, 0.01), 'Wareham': (50.68, -2.14), 'Warlingham': (51.3, -0.05), 'Warminster': (51.17, -2.18), 'Warrington': (53.4, -2.58), 'Warwick': (52.25, -1.58), 'Washington': (54.9, -1.52), 'Watchet': (51.16, -3.35), 'Waterlooville': (50.89, -1.02), 'Watford': (51.65, -0.39), 'Watlington': (51.65, -1.0), 'Wedmore': (51.22, -2.81), 'Wednesbury': (52.56, -2.02), 'Welling': (51.46, 0.1), 'Wellingborough': (52.3, -0.65), 'Wellington': (50.97, -3.24), 'Wells': (51.21, -2.65), 'Wells-Next-the-Sea': (52.94, 0.86), 'Welshpool': (52.65, -3.2), 'Welwyn': (51.83, -0.19), 'Welwyn Garden City': (51.8, -0.19), 'Wembley': (51.55, -0.29), 'West Bromwich': (52.53, -1.99), 'Westbury': (51.26, -2.17), 'West Byfleet': (51.33, -0.48), 'Westcliff-on-Sea': (51.54, 0.69), 'West Drayton': (51.5, -0.46), 'Westerham': (51.29, 0.05), 'Westgate-on-sea': (51.38, 1.34), 'West Malling': (51.29, 0.41), 'West Molesey': (51.4, -0.36), 'Weston-Super-Mare': (51.34, -2.94), 'West Wickham': (51.37, -0.01), 'Wetherby': (53.91, -1.37), 'Weybridge': (51.36, -0.44), 'Weymouth': (50.62, -2.46), 'Whitby': (54.46, -0.67), 'Whitchurch': (52.09, -2.0), 'Whitehaven': (54.54, -3.57), 'Whitland': (51.85, -4.61), 'Whitley Bay': (55.05, -1.46), 'Whitstable': (51.35, 1.03), 'Wickford': (51.61, 0.53), 'Widnes': (53.37, -2.74), 'Wigan': (53.53, -2.64), 'Wigston': (52.58, -1.11), 'Wigton': (54.8, -3.23), 'Willenhall': (52.59, -2.04), 'Wilmslow': (53.32, -2.23), 'Wimborne': (50.81, -1.97), 'Wincanton': (51.05, -2.4), 'Winchelsea': (50.92, 0.7), 'Winchester': (51.06, -1.31), 'Windermere': (54.37, -2.91), 'Windlesham': (51.36, -0.65), 'Windsor': (51.47, -0.62), 'Wingate': (54.72, -1.37), 'Winkleigh': (50.87, -4.0), 'Winscombe': (51.32, -2.82), 'Winsford': (53.19, -2.52), 'Wirral': (53.36, -3.09), 'Wisbech': (52.64, 0.17), 'Witham': (51.8, 0.63), 'Withernsea': (53.72, 0.03), 'Witney': (51.78, -1.46), 'Woking': (51.31, -0.56), 'Wokingham': (51.4, -0.84), 'Wolverhampton': (52.59, -2.15), 'Woodbridge': (52.14, 1.35), 'Woodford Green': (51.6, 0.03), 'Woodhall Spa': (53.15, -0.21), 'Woodstock': (51.85, -1.35), 'Wooler': (55.55, -2.04), 'Worcester': (52.18, -2.21), 'Worcester Park': (51.37, -0.24), 'Workington': (54.63, -3.53), 'Worksop': (53.31, -1.14), 'Worthing': (50.82, -0.39), 'Wotton-under-Edge': (51.62, -2.38), 'Wrexham': (53.04, -3.0), 'Wylam': (54.97, -1.81), 'Wymondham': (52.57, 1.11), 'Yarm': (54.49, -1.33), 'Yarmouth': (50.69, -1.47), 'Yateley': (51.33, -0.82), 'Yelverton': (50.5, -4.1), 'Yeovil': (50.95, -2.63), 'Y Felinheli': (53.18, -4.19), 'York': (53.99, -1.04), 'Ystrad Meurig': (52.23, -3.93)}
    '''
    Towndict = {}
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            city = row[0]
            latitude = float(row[1])
            longitude = float(row[2])
            Towndict[city] = (latitude, longitude)
    file.close() # prevent data leak
    return Towndict

def plotSpecificTowns(map, Towndict):
    """
        plot specific towns on a map using the town data dictionary.
        :param map: The map object on which towns will be plotted.
        :param Towndict: A dictionary containing town names and their corresponding geographical coordinates.
        :return: The updated map object with plotted towns.
    """
    sigCities = ("Aberystwyth", "London", "Cardiff", "Birmingham") # signifcant cities
    for town, (latitude, longitude) in Towndict.items():
        if town.endswith(("bury", "ampton")) or town.startswith(('A', 'B', 'C', 'L', 'M')):
            if town in sigCities:
                map.plot(longitude, latitude, marker='o', markersize=5, color="red")
            else:
                map.plot(longitude, latitude, marker='o')
    return map

def getWeatherResponse(apikey, city, days):
    '''
    gets the weather response from the weather apo
    :param apikey: the key for the weather api
    :param city: the specific city
    :param days: number of forcast days
    :return: the json response for the request of weather forecast
    '''
    try:# checks to see if the response was successful
        response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={apikey}&q={city}&days={days}")
        return response.json()
    except requests.RequestException as exceptionOutput:
        print("An error occurred" + str(exceptionOutput))

def displayWeatherForecast(apikey, cities, days):
    '''
    displays the weather forcast data for each city
    :param apikey: the key for the weather api
    :param cities: a list of the cities
    :param days: number of forcast days
    '''
    weatherData = WeatherForecast(apikey, cities, days)
    # display the weather info to the screen
    for city, data in weatherData.items():
        print("Weather forecast for " + city)
        for day in data["forecast"]["forecastday"]:
            for hour in day["hour"]:
                print("Time: "+str(hour["time"])+", Temperature: "+str(hour["temp_c"])+" C, Condition: "+str(hour["condition"]["text"]))
        print("\n")

def saveWeather(apikey, cities, days):
    '''
    saves the weather data for each city into a csv file which is output to the project directory
    :param apikey: the key for the weather api
    :param cities: a list of the cities
    :param days: number of forcast days
    :return: a csv file containing the weather data to the same directory as the python file
    '''
    weatherData = WeatherForecast(apikey, cities, days)
    for city in cities:
        if city in weatherData:
            filename = (city + ".csv")
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Date and time", "Weather condition", "Temperature"])
                for day in weatherData[city]["forecast"]["forecastday"]:
                    for hour in day["hour"]:
                        writer.writerow([hour["time"], hour["condition"]["text"], hour["temp_c"]])
            file.close() # prevent data leak

def WeatherForecast(apikey, cities, days):
    '''
    gets the weather forecast data for each city using weather response json
    :param apikey: the key for the weather api
    :param cities: a list of the cities
    :param days: number of forcast days
    :return: weatherData dictionary with cities as keys and the forecast data as values
    '''
    weatherData = {}
    for city in cities:
        forecast = getWeatherResponse(apikey, city, days)
        if forecast:  # check if forecast data was actually taken
            weatherData[city] = forecast
        else:
            print("forcast not receieved")
    return weatherData

def citiesWeatherCategories(weatherData):
    '''
    categorises the cities for the weather at the that city
    :param weatherData dictionary with cities as keys and the forecast data as values
    :return weatherCategories: a dictionary with the weather categories and lists filled with the cites of that weather category
    '''
    freezingTemp = 0 # freezing temp in celsius, for removing magic literals
    weatherCategories = {"raining": [], "snowing": [], "icing": [], "else": []} # initialise's a dictionary of the weather catagories and empty lists to fill later with cities
    for city, data in weatherData.items(): #categorise the weather data
        rainingHours = sum(1 for hour in data["forecast"]["forecastday"][0]["hour"] if ("rain") in hour["condition"]["text"].lower() or "drizzle" in hour["condition"]["text"].lower())
        snowingHours = sum(1 for hour in data["forecast"]["forecastday"][0]["hour"] if ("snow") in hour["condition"]["text"].lower() or "blizzard" in hour["condition"]["text"].lower())
        icingHours = sum(1 for hour in data["forecast"]["forecastday"][0]["hour"] if hour["temp_c"] < freezingTemp)
        if rainingHours >= 6: # specific weather hours as mentioned in brief
            weatherCategories["raining"].append(city)
        elif snowingHours >= 4:
            weatherCategories["snowing"].append(city)
        elif icingHours > 8:
            weatherCategories["icing"].append(city)
        else:
            weatherCategories["else"].append(city)
    #displaySuggestions(weatherCategories) # used for testing output needs to be commented out
    return weatherCategories

def displaySuggestions(weatherCategories):
    '''
    Displays the weather suggestions for the weather type at each city
    :param weatherCategories: a dictionary with the weather categories and lists filled with the cites of that weather category
    :return: printed messages to the screen
    '''
    if weatherCategories["raining"]:
        print("Bring your umbrella if you are in these cities:")
        print("\n".join(weatherCategories["raining"])) # prints all elements in raining on a new line
        print("\n")
    if weatherCategories["snowing"]:
        print("Plan your journey thoroughly if you are in these cities:")
        print("\n".join(weatherCategories["snowing"])) # prints all elements in snowing on a new line
        print("\n")
    if weatherCategories["icing"]:
        print("Mind your step if you are in these cities:")
        print("\n".join(weatherCategories["icing"])) # prints all elements in icing on a new line
        print("\n")
    if weatherCategories["else"]:
        print("Enjoy the weather if you are in these cities:")
        print("\n".join(weatherCategories["else"])) # prints all elements in else on a new line
        print("\n")


def presentXML(weatherCategories):
    '''
    Creates and saves the weather data with messages in a XML file
    :param weatherCategories: a dictionary with the weather categories and lists filled with the cites of that weather category
    :return: the xml file containing the weather messages and cities
    '''
    currentdate = datetime.now().strftime("%Y-%m-%d")
    weatherForecasting = ET.Element("WeatherForecasting")
    Date = ET.SubElement(weatherForecasting, "Date", Date=currentdate)

    if weatherCategories["else"]: # conditional statement to check the category
        goodWeather = ET.SubElement(Date, "GoodWeather")
        goodWeather.text = "Enjoy the weather if you are in these cities" # weather category message
        gCities = ET.SubElement(goodWeather, "cities")
        for city in weatherCategories["else"]: # makes all cities in this category a sub element in the tree
            ET.SubElement(gCities, "city", name=city)
    if weatherCategories["raining"]:
        poorWeatherR = ET.SubElement(Date, "PoorWeather", Issue="Raining")
        poorWeatherR.text = "Bring your umbrella if you are in these cities"
        pCitiesR = ET.SubElement(poorWeatherR, "cities")
        for city in weatherCategories["raining"]:
            ET.SubElement(pCitiesR, "city", name=city)
    if weatherCategories["icing"]:
        poorWeatherI = ET.SubElement(Date, "PoorWeather", Issue="Icing")
        poorWeatherI.text = "Mind your step if you are in these cities"
        pCitiesI = ET.SubElement(poorWeatherI, "cities")
        for city in weatherCategories["icing"]:
            ET.SubElement(pCitiesI, "city", name=city)
    if weatherCategories["snowing"]:
        poorWeatherS = ET.SubElement(Date, "PoorWeather", Issue="Snowing")
        poorWeatherS.text = "Plan your journey thoroughly if you are in these cities"
        pCitiesS = ET.SubElement(poorWeatherS, "cities")
        for city in weatherCategories["snowing"]:
            ET.SubElement(pCitiesS, "city", name=city)
    # write xml file using python 3.10
    xmlTree = ET.tostring(weatherForecasting, encoding='unicode')
    xmlTree = minidom.parseString(xmlTree).toprettyxml(indent="   ")
    with open(currentdate + ".xml", "w", encoding='UTF-8') as f:
        f.write(xmlTree)
    f.close() # prevent data leak

def importUserData_csv(filename):
    '''
    imports the user data from the csv file users.csv
    :param filename: the file name of the user data file users.csv or its path to the file
    :return: a dictionary with city names as the keys and the count of users in that city as the values
    >>> importUserData_csv('users.csv')
    {'Bristol': 220, 'York': 236, 'London': 233, 'Lichfield': 235, 'Gloucester': 237, 'Dundee': 233, 'Belfast': 236, 'Hereford': 236, 'Carlisle': 229, 'Wolverhampton': 225, 'Stoke-On-Trent': 238, 'Brighton And Hove': 208, 'Plymouth': 218, 'Westminster': 250, 'Canterbury': 232, 'Inverness': 224, 'Preston': 236, 'Cardiff': 230, 'Leicester': 233, 'Newcastle Upon Tyne': 205, 'Portsmouth': 210, 'Manchester': 225, 'Chichester': 228, 'Derby': 249, 'St Albans': 252, 'Armagh': 233, 'Kingston Upon Hull': 223, 'Norwich': 236, 'Glasgow': 252, 'Ripon': 226, 'Coventry': 242, 'Londonderry': 232, 'Exeter': 206, 'Salisbury': 220, 'Winchester': 233, 'Bradford': 241, 'Liverpool': 239, 'Salford': 227, 'Wakefield': 206, 'Sheffield': 240, 'Bath': 233, 'Newry': 240, 'Worcester': 218, 'Cambridge': 240, 'Aberdeen': 231, 'Durham': 220, 'Bangor': 237, 'Wells': 248, 'Lisburn': 253, 'Stirling': 222, 'Nottingham': 249, 'Lincoln': 225, 'Chester': 225, 'Birmingham': 191, 'Edinburgh': 258, 'Southampton': 227, 'Oxford': 198, 'Ely': 230, 'St Davids': 235, 'Swansea': 247, 'Leeds': 240, 'Peterborough': 214, 'Truro': 219, 'Sunderland': 228, 'Newport': 258}
    '''
    userCount = {}
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            city = row["location.city"].title()
            if city == ("City Of London"): # replaces city of london names, fixes naming error
                city = "London"
            userCount[city] = userCount.get(city, 0) + 1
    file.close() # prevent data leak
    return userCount

def plotWeatherDataOnMap(map, user_count, weatherCategories, Towndict):
    '''
    plots the weather data on the map making the size of the marker related the user count and marker type based on the weather
    :param map: the map object the data will be plotted on
    :param user_count: a dictionary containing the users counts for teh cities
    :param weatherCategories: a dictionary with the weather categories and lists filled with the cites of that weather category
    :param Towndict: A dictionary containing town names and their corresponding geographical coordinates
    :return: The updated and plotted map object to be displayed
    '''
    for category, cities in weatherCategories.items():
        for city in cities:
            if city in Towndict and city in user_count:
                latitude, longitude = Towndict[city]
                #markersize = np.log(user_count[city])
                markersize = round(user_count[city]*0.05)
                # plots data on the map with a variable marker size
                if weatherCategories["raining"]:
                    map.plot(longitude, latitude, marker='v', markersize=markersize, color="red")
                if weatherCategories["snowing"]:
                    map.plot(longitude, latitude, marker='d', markersize=markersize, color="blue")
                if weatherCategories["icing"]:
                    map.plot(longitude, latitude, marker='*', markersize=markersize, color="cyan")
                if weatherCategories["else"]:
                    map.plot(longitude, latitude, marker='o', markersize=markersize, color="green")
    return map

if __name__ == "__main__":
    print("Start Main")
    # task 1
    # filename = "latlon.csv"
    # Towndict = importTownData_csv(filename)
    # #print(Towndict)
    # map = plotSpecificTowns(UKMap.UKMap(), Towndict)
    # map.show()

    # task 2+3
    # apikey = ("fd8002b7f80a4eb695d220522232912")
    # cities = ("Aberystwyth", "Bangor", "Birmingham", "Cardiff", "Derby", "Leeds", "London", "Manchester", "Swansea")
    # displayWeatherForecast(apikey, cities, 3) # three days
    # saveWeather(apikey, cities, 3)

    # task 4 + 5
    # apikey = ("fd8002b7f80a4eb695d220522232912")
    # cities = ("Aberystwyth", "Bangor", "Birmingham", "Cardiff", "Derby", "Leeds", "London", "Manchester", "Swansea")
    # numDays = 3 # three days
    # weatherCategories = citiesWeatherCategories(WeatherForecast(apikey, cities, numDays)) # three days
    # displaySuggestions(weatherCategories)
    # presentXML(weatherCategories)

    #task 6
    apikey = ("fd8002b7f80a4eb695d220522232912")
    cities = ("Aberystwyth", "Bangor", "Birmingham", "Cardiff", "Derby", "Leeds", "London", "Manchester", "Swansea")
    filename = "latlon.csv"
    userfilename = "users.csv"
    userCount = importUserData_csv(userfilename)
    Towndict = importTownData_csv(filename)
    numDays = 1 # one day
    weatherCategories = citiesWeatherCategories(WeatherForecast(apikey, cities, numDays)) # one day
    map = plotWeatherDataOnMap(UKMap.UKMap(), userCount, weatherCategories, Towndict)
    map.show()
    doctest.testmod()
