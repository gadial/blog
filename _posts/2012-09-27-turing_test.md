---
id: 2192
title: "מבחן טיורינג"
date: 2012-09-27 08:06:26
layout: post
categories: 
  - בעיות מתמטיות מפורסמות
  - ההיסטוריה של המתמטיקה
  - מתמטיקה בראי התקשורת
tags: 
  - בינה מלאכותית
  - יותר מדי לא מדויק
  - מבחן טיורינג
---
אלן טיורינג, שהשנה חגגנו את יום הולדתו ה-100, היה מחשובי המדענים של המאה ה-20. במאמר מ-1936 הוא הניח את היסודות לתיאוריה של מדעי המחשב, ובאותה ההזדמנות גם נתן השראה לחלוצים שמבין בוני המחשבים הפיזיים. בשנות מלחמת העולם השניה הוא היה אחד מהבולטים שבמפצחי הצפנים של אנגליה בבלצ'לי פארק ובכך תרם תרומה חשובה לניצחון בעלות הברית במלחמה. פרט לכך הוא התעסק בעוד המוני דברים אחרים. עם זאת, דומני שאת טיורינג רובו של הציבור הרחב מכיר בראש ובראשונה דרך <strong>מבחן טיורינג</strong> הנושא את שמו, למרות שאיני בטוח אם טיורינג עצמו היה מחשיב את המבחן לאחד מהחשובים שברעיונותיו. למרות זאת המבחן מעניין והגיע הזמן להקדיש לו פוסט.

המוטיבציה העדכנית שלי מגיעה מ"ליל המדענים" שנערך בישראל ביום שני האחרון, ובמסגרתו שודר שעשועון בשם "<a href="http://www.ynet.co.il/articles/0,7340,L-4285808,00.html">אדם מול מכונה</a>" שבלי ספק התקיים בהשראת מבחן טיורינג. מכיוון שבדיווח של Ynet השעשועון זכה לכותרות של "המחשב הצליח להערים על בני האנוש", נכתב כי השעשועון "מדמה מבחן טיורינג" ואפילו שר המדע והטכנולוגיה, המתמטיקאי דניאל הרשקוביץ צוטט כאומר ש"ניתן להגיד בהסתייגות זהירה כי המחשב עבר את מבחן טיורינג, לפחות בשעשועון זה", אני חושב שלא יזיק להעמיד דברים על דיוקם, להסביר מה הרעיון במבחן טיורינג ולמה שעשועון ה"אדם מול מכונה" הוא <strong>ממש לא</strong> מבחן טיורינג ותוצאותיו לא ממש אומרות משהו.

מבחן טיורינג, בבסיסו, הוא מבחן שבו מתחרים מחשב ובן אדם. הם מתקשרים עם בוחן אנושי באמצעות מסך צ'אט, והבוחן שואל אותם שאלות, כאשר מטרתו היא להבין מי האדם ומי המחשב. אם הבוחן הצליח לגלות מיהו המחשב, המחשב "הפסיד"; אם הבוחן אינו מסוגל להגיע להכרעה או שהוא טועה, המחשב "מנצח", או בלשון היותר נייטרלית שבה אשתמש - עובר את מבחן טיורינג. כמובן שמבחן אחד לא מספיק - צריך לחזור על המבחן עם הרבה בוחנים שונים כדי להגיע למסקנה סבירה כלשהי.

[caption id="attachment_2201" align="aligncenter" width="320"]<img class="size-full wp-image-2201 aligncenter" title="turing_test" src="{{site.baseurl}}{{site.post_images}}/2012/09/turing_test.png" alt="" width="320" height="394" /> מבחן טיורינג, גרסת xkcd.[/caption]

את המבחן הזה הציע טיורינג במאמר ששמו Computing Machinery and Intelligence משנת 1950 וניתן לראות <a href="http://loebner.net/Prizef/TuringArticle.html">כאן</a>. המאמר הוא קריא ולא טכני יחסית (יחסית! יש בו חלקים טכניים באמצע שלטעמי הם מיותרים למדי) ואני ממליץ לכולכם לתת לו צ'אנס. המאמר עצמו פורסם בכתב עת פילוסופי, לא מתמטי, ונכתב בצורה לא-פורמלית למדי; לדעתי טיורינג עצמו לא לקח את המאמר יותר מדי ברצינות, מתוך הכרה בכך שהשאלה שהוא מנסה להתמודד איתה היא כבדה מדי מכדי שתוכל להיות מוכרעת באמצעות המבחן. ומה השאלה הזו? טיורינג פותח איתה את המאמר - זוהי השאלה "האם מכונות יכולות לחשוב?".

זו שאלה קשה, קשה ביותר, ועם השלכות לא פשוטות כלל (למשל, אם מכונות אכן מסוגלות לחשוב, האם יש להן תודעה? אם כן, האם זה מוסרי לכבות אותן?). כפי שטיורינג מציין היטב בפתח המאמר, לב הבעיה בהתמודדות עם השאלה הזו היא שלא ברור לנו מהי "מכונה" (האם אדם איננו בסופו של דבר מכונה מורכבת? והאם מחשב שייבנה מרקמות ביולוגיות עדיין יקרא "מכונה"?) ולא ברור לנו מה פירוש המילה "לחשוב". העובדה שהמילים הללו לא מוגדרות מונעות מראש כל דיון מתמטי בנושא. על כן, טיורינג רצה להתחמק מהשאלה הזו על ידי מעבר לשאלה אחרת שאפשר להתמודד איתה בצורה יותר מדויקת. הרעיון שלו הגיע ממשחק חברה שהיה מוכר בזמנו, שבו גבר ואישה מנהלים שיחה עם "בוחן" - ושוב, דרך צ'אט (בזמנו של טיורינג לא היה צ'אט אז הוא מדבר על חדרים נפרדים ושאלות ותשובות שנכתבות במכונת כתיבה), ומטרת הבוחן היא לגלות מי הגבר ומי האישה. כמובן שהשחקנים <strong>לא חייבים להיות דוברי אמת</strong> (אחרת הבוחן יכול פשוט לשאול "האם אתה גבר?") וזה מה שמעניק למשחק הזה את העניין שבו. ההנחה היא שאחד השחקנים רוצה לעזור לבוחן להצליח, בעוד שהשחקן השני הוא הנבחן האמיתי, ומטרתו היא להטעות את הבוחן.

אם כן, כל מה שטיורינג הציע הוא לקחת את המשחק הזה ולשחק אותו עם מחשב ובן אדם. את כל זה הוא עושה בעמוד הראשון של המאמר. אם כן, מה הוא עושה בעשרים העמודים הנותרים? בעיקר מנסה לשכנע את הקורא שהמבחן הוא מעניין ולהתייחס להתנגדויות המובנות מאליהן אליו ואל התפיסה שמחשבים יכולים לחשוב (ובאופן מרתק למדי, הוא מכסה פחות או יותר כל טיעון ששמעתי עד היום בנושא; אולם נגיע לכך בהמשך).

טיורינג מעלה מייד כמה נקודות ברורות בנוגע למבחן:
<ul>
	<li>המבחן מסנן החוצה כל אספקט "פיזיקלי" של ההבדלים בין אנשים ומכונות. גם בימינו, שישים שנים לאחר המאמר של טיורינג, עדיין אין רובוטים שנראים באופן מושלם כמו בני אדם (אם כי חייבים להודות שהתחום התפתח בצורה מרשימה). כל רובוט בימינו היה כנראה מפסיד את המבחן מייד בשל המראה שלו, בלי קשר לשאלה האם הוא מסוגל לחשוב או לא. לכן עניין ההפרדה ופורמט התשובות (צ'אט) הוא קריטי למדי.</li>
	<li>המבחן מוטה מאוד <strong>לרעת</strong> המכונה; בבירור, אם המצב היה הפוך, והמבחן היה כולל אדם שמנסה להתחזות למכונה הוא היה מפסיד מייד, מכיוון שמכונות מסוגלות לבצע חישובים במהירות אדירה בהרבה אפילו מאנשים שהם מחשבונים אנושיים. טיורינג מסכים שההטיה הזו קיימת, אבל הדבר אינו בעייתי באמת כי זה רק אומר ש<strong>אם</strong> מכונה כלשהי תעבור את המבחן, ההישג שלה יהיה מרשים אף יותר (כמו כן, לדעתי ההטייה הזו מעידה על ההבדל בין "חשיבה" ו"חישוב" עבורנו, אף שכלל לא ברור שברמה הבסיסית ביותר אין מדובר על אותו הדבר).</li>
	<li>לדעת טיורינג, ההנחה לפיה הדרך הטובה ביותר לנצח במשחק היא אכן לענות תשובות שבן אדם היה עונה היא הנחה סבירה מספיק כדי שלא לחקור אפשרויות אחרות. אני אישית נוטה להסכים עם טיורינג ולא זכורה לי ביקורת על המבחן שבאמת הולכת לכיוון הזה.</li>
</ul>
מה שטיורינג <strong>לא</strong> אומר הוא שמכונה שעוברת את המשחק אכן מסוגלת לחשוב. זו הסקת מסקנות חפוזה למדי! אם כבר ההפך הוא נכון - מכונה שמסוגלת לחשוב, סביר להניח שתעבור את המבחן.

כעת, בואו נעזוב לעת עתה את המאמר של טיורינג וננסה לראות האם הבנו את הרעיון של המבחן (ולמה הוא כל כך מוצלח) דרך התבוננות במשחק ה"אדם מול מכונה" והבנה של הדרכים הרבות שבהן הוא שונה מהמבחן של טיורינג.

בעיה בסיסית במבחן טיורינג היא שהוא אינו מצטלם טוב. מה, נצלם איש באולפן מקליד שאלות לצ'אט ומקבל תשובות? זה כנראה בלתי נסבל לחלוטין עבור מי שמעוניינים בפופולריזציה של מדעי המחשב, וזו הייתה מטרתם של עורכי המשחק. אין לי ספק שזו מטרה ראויה ביותר, וגם אין לי ספק שהבחירה בפופולריזציה הזו על חשבון התוכן האמיתי של המבחן הייתה מכוונת; לא אחזור על ההבהרה הזו בכל פעם מחדש. אני לא מעוניין למתוח ביקורת על המשחק עצמו, אלא רק להבהיר למה הוא שונה ממבחן טיורינג (ולכן אני <strong>כן</strong> מעוניין למתוח ביקורת על כל מי שניסו להקביל אותו למבחן טיורינג, בציטוטים שהבאתי).

ב"אדם מול מכונה" שינו את הפורמט של המבחן כדי שיהיה מעניין יותר. במקום בוחן מול צ'אט, יש באופן בוחן מול ארבעה שחקנים. השאלות ניתנות לשחקנים מראש ובשידור עצמו הם רק מקריאים את התשובות שלהם. בנוסף לכך, אחד מהשחקנים הוא "רמאי" והוא אינו מקריא את התשובות שלו אלא את התשובות של המחשב. המטרה של הצופים בבית היא לזהות מי המחשב. בפועל, רק 27 אחוז מהמצביעים הצליחו לזהות נכון את השחקן שהוא המחשב ורוב הקולות הלכו בכלל לשחקן אחר, כך שאין ספק שהמחשב "ניצח" במשחק הזה. אבל האם זו חוכמה?

יש בעיה לא קטנה בלתת לאדם להקריא את התשובות של המחשב כאילו הן התשובות שלו, ועוד שיהיה זה אדם שאנחנו רואים בעיניים ואפילו יודעים מה הרקע שלו. זה מוסיף למשחק את שאלת ההתאמה של תשובות המחשב לתשובות שאנחנו <strong>מצפים</strong> שהאדם יתן. במקרה או שלא במקרה, התשובות של המחשב ניתנו לילד לא מוכר, שאין לנו ציפיות מוקדמות שכאלו לגביו (לפחות בעיני, הדבר הופך אותו אוטומטית ל"חשוד").

אבל הבעיה העיקרית כאן היא שהעובדה שהשאלות נשאלו מראש מונעת מהדיון <strong>להתפתח</strong>. אני אישית חושב שעיקר הכוח של מבחן טיורינג היא בכך שהבוחן יכול לשאלות שאלות חדשות <strong>בהתבסס</strong> על התשובות של הנבחן. זה מאפשר לשאול שאלות עמוקות יותר ולתפוס את הנבחן בסתירות פנימיות. במקרה שלנו, למרות שזה בלתי אפשרי, התחושה שלי הייתה שהמנחה <strong>אכן שאל</strong> שאלות חדשות בהתבסס על התשובות של הנבחן, אם כי לא רציניות במיוחד; למשל, לשאלה על אישיות נערצת הילד (כלומר, המחשב) השיב "טיורינג" והמנחה שאל "למה" (למרות שהוא לא שאל זאת את המשתתפים האחרים). הילד ענה תשובה כלשהי; אין לי מושג אם זו תשובה שאכן הגיעה מהמחשב עצמו או שהילד המציא אותה בו במקום. רואים את הבעייתיות? אם ה"מקריא" יתחיל לענות תשובות שהוא עצמו ממציא, המבחן כולו הולך לאבדון. זה ממחיש יפה עד כמה פורמט עריכת המבחן שהציע טיורינג הוא אפקטיבי; לצערי, אני לא מסוגל לחשוב על שום דרך טובה לשנות אותו (חוץ מאשר לתת לרובוטים דמויי אדם להקריא את <strong>כל</strong> התשובות, במקום שנראה חלון צ'אט).

בעיה משמעותית הרבה יותר במבחן היא השאלות עצמן. חצי מהמבחן כלל שאלות טריוויה. בעבר היה ערך לשאלות כאלו כי הן יכלו להצביע על ידע שאנחנו מצפים ש"לכל אדם יהיה" לפחות חלק ממנו אבל למחשבים פשוט לא היה. מהפכת המידע שינתה את כל זה. במאמר של Ynet הזכירו את התוכנה "ווטסון" שפותחה במעבדות IBM. ווטסון מסוגל לענות לשאלות טריוויה שנשאלות בשפה טבעית (כלומר, גם "להבין" בדיוק מה שאלו אותו, וגם למצוא את התשובה) וזאת בסיוע מאגר מידע עצום בגודלו (שכולל, למשל, את כל ויקיפדיה), אם כי בלי חיבור אינטרנט. כמה טוב הוא עושה זאת? טוב מספיק כדי לנצח בשעשועון הטריוויה Jeoprady. זה הישג אדיר של תחום הבינה המלאכותית ואחד מהדברים המגניבים ביותר במדעי המחשב, לדעתי. זה בפירוש <strong>לא</strong> משהו שעובר את מבחן טיורינג. אפילו לא קרוב. הדבר דומה למחשבים שמשחקים שחמט מצוין - הם מאוד טובים במטלה ספציפית שקיימים אלגוריתמים טובים עבורה; אנחנו עדיין לא קופצים מכך ל"חשיבה" באופן כללי. לכן כל שאלות הטריוויה היו בעלות ערך בדיוק כמו לראות את אחד מהמשתתפים מנצח בשחמט. פרט לכך, היו יחסית מעט שאלות טריוויה ואפילו אם המחשב לא היה יודע לענות על אף אחת מהן, כל עוד הוא היה "מתנצל" בצורה משכנעת כנראה לא היה מתעורר בנו חשד (ואכן, אחת השחקניות לא ידעה לענות על רוב שאלות הטריוויה ואיני חושב שזה גרם למישהו לחשוד שהוא מקריאה תשובות של מחשב).

אם כן, חלק חשוב ממבחן טיורינג הוא בוחן ששואל שאלות <strong>טובות</strong>. זו לא חוכמה להוליך שולל בוחנים ששואלים שאלות שהן לא משהו. כדאי לשים לב לכך שמחשבים מוליכים אותנו שולל גם בימינו; כבר נרשמו מקרים לא מעטים שבהם אדם שוחח עם רובוט באינטרנט בלי להבין שהוא לא מדבר עם בן אנוש; וכבר בשנות השישים התפרסמה התוכנית <a href="http://en.wikipedia.org/wiki/ELIZA">ELIZA</a> שהייתה תוכנית שיחה פשטנית ביותר שעדיין הצליחה להוליך שולל לא מעט מהמשוחחים איתה שהאמינו שהם מדברים עם פסיכולוג אמיתי בשר ודם. בנוסף, ראוי שמי שמכריע את המבחן יהיה גם זה ששואל את השאלות (ולכן כנראה שואל את הדברים שהכי עוזרים <strong>לו</strong> להכריע) - לתת לקהל להחליט, למרות שלא הקהל הוא זה ששאל את השאלות באופן אישי, הוא עוד מרכיב מהבעיה. הרי אם המחשב עובר את המבחן הזה, זה יכול להעיד בעיקר על כך שרצף השאלות הספציפי שנשאל במבחן הוא לא טוב מספיק כדי להכריע בין המחשב והאנשים (ולדעתי הוא אכן היה בעייתי). אני בהחלט מבין למה עורכי המשחק עשו זאת כך - לשתף את הקהל בהכרעה זה מרכיב חשוב של השעשוע - אבל את המבחן עצמו זה מקלקל.

[caption id="attachment_2204" align="alignnone" width="717"]<a href="{{site.baseurl}}{{site.post_images}}/2012/09/klingon_turing_test.png"><img class="size-full wp-image-2204" title="klingon_turing_test" src="{{site.baseurl}}{{site.post_images}}/2012/09/klingon_turing_test.png" alt="" width="717" height="941" /></a> גם במבחן טיורינג לקלינגונים יש בעיות עם השאלות (ותודה ל-Abstrusegoose).[/caption]

ובכן, איך אמור מבחן טיורינג "אמיתי" עם שאלות טובות להיראות? אני מרשה לעצמי לצטט מתוך ספרו של פרופ' דוד הראל (שהיה מעורב בהכנת "אדם מול מכונה"), "המחשב אינו כל יכול" (אותו הטקסט הופיע בניסוח כמעט זהה גם ב"אלגוריתמיקה" של דוד הראל - ספר שעליו אני ממליץ בחום והוא מה שגרם לי להתעניין במדעי המחשב מלכתחילה) דיאלוג קצר בין הבוחנת איה והמתמודד בועז:
<blockquote>איה: מה זה שלכטיון?
<!--more-->
בועז: אין לי מושג.

איה: שלכטיון הוא לוויתן מעופף שכותב סיפורים. הוא פותח במעבדה, בתהליך קפדני שנמשך כמה דורות כדי להבטיח שסנפיריו יתפתחו לאיברים דמויי כנף שיאפשרו לו לעוף. כמו כן, לימדו אותו בהדרגה קרוא וכתוב. הוא בעל ידע נרחב בספרות מודרנית ומסוגל לכתוב סיפורי מסתורין ראויים לפרסום.

בועז: מוזר מאוד.

איה: האם אתה חושב ששלכטיונים קיימים?"

בועז: מה פתאום, אין סיכוי.

איה: מדוע?

בועז: מסיבות רבות. ראשית, יכולות ההנדסה הגנטית שלנו אפילו אינן מתקרבות למה שנדרש להפיכת סנפירים לכנפיים, שלא לדבר על חוסר היכולת שלנו לגרום ליצורים חסרי מנוע במשקל עשרה טון להפר את כוח המשיכה פשוט על ידי נפנוף באיברים שכאלה. שנית, החלק הנוגע לכתיבת סיפורים אינו ראוי אפילו לתגובה, כיוון שכתיבת סיפור טוב דורשת הרבה יותר מאשר יכולת טכנית לקרוא ולכתוב. הרעיון כולו נשמע מגוחך. אין לך נושאי שיחה מעניינים יותר?</blockquote>
חשבו קצת מה התגובה המנומקת של בועז דורשת. לא רק היכרות עם פרטי טריוויה (למשל, שלוויתן שוקל עשרה טון) אלא גם הבנה שלהם והאופן שבו הם מתחברים זה לזה - <strong>ידע</strong> ולא רק <strong>מידע</strong>. אפשר לטעון שרוב המתמודדים האנושיים לא יגיעו לרמה של בועז בכל הנוגע לאיכות התשובות שלהם, מה שכמובן מצביע על כך שרצוי שבמבחן טיורינג ישתתף לא רק בוחן נבון אלא גם מתמודד נבון כנגד המחשב; אבל הדוגמה הזו היא קיצונית מעט בגלל שה"מבחן" כאן הוא קצר מאוד, ובמבחנים ארוכים יותר אפשר לתת שאלות קצת פחות מאתגרות שעדיין ידרשו יכולת חשיבה שלמחשבים בני זמננו פשוט אין.

הדגש כאן, אם כן, הוא על תשובות <strong>מורכבות</strong>, שאינן התחמקות מהשאלה אלא התייחסות ישירה אליה, ורצוי כזו שמביאה בחשבון פרטים שמתקשרים אל השאלה בצורה לא טריוויאלית ולא נכללו בניסוח שלה מלכתחילה. במבחן של "אדם מול מכונה" לא היה שום דבר כזה. מה שכן ניסו לעשות הוא לשאול שאלות על נושאים שלא סביר שמחשב, שלא מנהל חיים אנושיים, ידע לענות עליהן - למשל, מה עושים כשבן הזוג כועס על כך ששכחת תאריך מיוחד. המחשב פשוט ענה שאין לו עדיין חברה, כלומר התחמק; בגלל שהדובר בשם המחשב היה ילד קטן התשובה נראתה סבירה (מדובר בוגר יותר היינו מצפים לנסיון תשובה כלשהו אפילו אם לדובר עצמו מעולם לא הייתה חברה).

בקיצור, נראה לי שברור לנו כבר שהמבחן של "אדם מול מכונה" הוא לא מבחן טיורינג ורק שואב ממנו קצת השראה. אני מקווה שאת מטרתו האמיתית - לעורר עניין באנשים - הוא השיג. בואו נחזור כעת לעסוק בטיורינג עצמו ובמאמר שלו. אחרי הצגת המבחן והתייחסות בסיסית אליו, טיורינג עובר לתיאור מדוקדק של "מהי מכונה" מבחינתו. זהו החלק הטכני במאמר, וכזה שרלוונטי הרבה פחות בימינו, שבהם מחשבים נמצאים בכל פינה. זכרו שטיורינג עצמו כתב את מאמרו המפורסם מ-1936 על מכונות טיורינג כאשר המחשבים לא היו קיימים בכלל (מכונת טיורינג עצמה היא מעין מחשב חצי אבסטרקטי, והיא כנראה הדבר הכי דומה למחשבים שהיה קיים לפני שהיו מחשבים) וגם ב-1950, שנת כתיבת המאמר על מבחן טיורינג, עדיין היה מדובר על מפלצות ענק נדירות יחסית. לכן, אם אתם קוראים את המאמר ואתם מתקשים בסעיפים 3-5, פשוט דלגו עליהם; עיקר האקשן מגיע בסעיף 6 שהוא כל כך מוצלח שאני רוצה לתאר פה את רובו (אבל שוב, עדיף לקרוא את טיורינג עצמו).

סעיף 6 עוסק בביקורות אפשריות על השאלה "האם מכונות יכולות לחשוב" ועל הוריאציה שלה שבאה לידי ביטוי במבחן טיורינג. לדעתי זה החלק המעניין ביותר במאמר, ולכן אתאר את כולו.
<ul>
<li>
<p>
הטיעון הדתי: "חשיבה היא פונקציה של נשמתו של האדם. אלוהים נתן את הנשמה לאדם, אבל לא למכונות, ולכן הן אינן יכולות לחשוב". כמובן שהטיעון הזה בעייתי מכל נקודת מבט אפשרית והוא בבסיסו הנחת המבוקש; אבל טיורינג מציין, ובצדק, שגם אם אלוהים <strong>עדיין</strong> לא נתן נשמה למכונה אין סיבה להניח שהוא לא יעשה זאת בעתיד, נניח אם המכונה תעבור את מבחן טיורינג. כך ש<strong>אפילו</strong> אם קיום נשמה הוא תנאי הכרחי לחשיבה, זה עדיין לא מסביר מדוע מכונות אינן יכולות, בעיקרון, לחשוב.</li>
</p>
<li>
<p>
טיעון ה"ראש בחול": "ההשלכות של כך שמכונות יכולות לחשוב הן איומות. הבה ונקווה שזה לא כך". גם זה, כמובן, לא טיעון רציני (אבל ההשלכות של קיום מכונות חושבות הן אכן רציניות, כפי שאמרתי בתחילת הפוסט). טיורינג מציין שהטיעון הזה לא ממש נאמר במפורש על ידי אנשים, אבל כולנו לוקים בו במידה מסויימת, מכיוון שהיינו שמחים להאמין שהאדם, בצורה כלשהי, נעלה על יתר הבריאה; ויכולת החשיבה שלנו היא המעלה היחידה שיש לנו שאין ליצורים אחרים בטבע. בכל פעם שאתם קוראים טיעון כלשהו נגד התפיסה לפיה מכונות יכולות לחשוב, כדאי לפקוח עיניים ולחפש האם "טמינת הראש בחול" הזו מסתתרת אי שם בטיעון הזה.
</p>
</li>

<li>
<p>
הטיעון המתמטי: כאן טיורינג מתייחס ישירות לנסיונות להשתמש בתוצאות מתמטיות כמו משפטי אי השלמות של גדל או אי-כריעות בעיית העצירה (שהוא עצמו הוכיח) כהמחשה לכך שהאדם מסוגל לחשיבה שמכונות אינן מסוגלות לה. התשובה הפשוטה של טיורינג היא זו: אמנם הוכיח שיש מגבלות חישוביות על המחשבים, אבל למרות שנטען כך, מעולם לא הוכח שהמגבלות הללו <strong>אינן חלות</strong> על האינטלקט האנושי. טיורינג אמר זאת ב-1950, ולמיטב ידיעתי גם למעלה משישים שנים לאחר מכן לא נמצאה כל הוכחה כזו (ו<strong>הוכחה </strong>היא מה שחייבים לספק; הרי אנחנו עוסקים כאן במתמטיקה).
</p>
<p>
בשעתו דיברתי בבלוג על <a href="http://www.gadial.net/2011/04/21/against_penrose_emperor_1/">טיעון מתמטי</a> של רוג'ר פנרוז שנופל בדיוק בקטגוריה הזו; למרות שהטיעון היה בנוי היטב אני סבור שיש בו כשלים (שעליהם ניסיתי להצביע בפוסט שלי ובפוסט ההמשך שלו) שבסופו של דבר מובילים אותנו בדיוק אל התשובה של טיורינג. פנרוז מצביע על מגבלה אבל מניח באופן מובלע שהיא אינה חלה על האינטלקט האנושי, מבלי שיוכיח זאת.
</p>
<p>
כמובן, טיורינג הוא קצת סלחני כאן ומתייחס רק לטיעונים המתמטיים הטובים; טיעונים <strong>שגויים לחלוטין </strong>שמסתמכים על משפטי גדל או על בעיית העצירה או על דברים דומים ונובעים מחוסר הבנה מוחלט שלהם יש למכביר, ועדיף לא להכביר עליהם מילים.
</p>
<p>
בנוסף, טיורינג מציין בחוכמה שגם אם <strong>יש</strong> מגבלות חישוביות על המחשב שאין על האדם, זה עדיין לא משכנע אותנו בכך שמכונות אינן יכולות לחשוב; בסופו של דבר, בני אדם בשר ודם שחושבים בלי צל של ספק עדיין עושים טעויות ולא מצליחים לענות על שאלות חישוביות ללא הרף.
</p>

<li>
<p>
הטיעון מן התודעה: זה כנראה סוג הטיעונים הנפוץ ביותר בדיונים פופולריים בנושא. הטענה היא שבגלל שמכונות אינן יכולות לחוש רגשות (או באופן כללי יותר, להיות בעלות תודעה) הן אינן חושבות "באמת". המהדרין מוסיפים ואומרים שאפילו אם יהיה בתוך המכונה מכניזם כלשהו שמנסה לדמות אושר, עצב, כאב וכו', זה לא יהיה "הדבר האמיתי". טיורינג מצביע על כך שהטיעון הזה הוא בעצם, במובלע, פסילה מוחלטת של מבחן טיורינג; שאם נקצין את הטיעון, נראה שהדרך היחידה שבה ניתן להיות בטוחים שמכונה חושבת היא <strong>להיות</strong> המכונה.
</p>
<p>
אם כן, השאלה אם לקבל את מבחן טיורינג או לא בתור דבר מה בעל ערך תלויה בשאלה אם אנחנו מאמינים שניתן להשתכנע בקיום חשיבה אצל מישהו רק על בסיס שיחה איתו. אם כן, כמובן שמבחן טיורינג הגיוני; אם לא, אנחנו נדחפים לבעיות מהותיות הרבה יותר מאשר "האם מכונות יכולות לחשוב"; אנחנו נאלצים גם לתהות אם האנשים שמסביבינו אכן חושבים או שהם רק רובוטים בשר ודם שפשוט מאוד דומים לי ולכן טבעי עבורי להניח שגם הם חושבים כמוני (ומי מאיתנו לא תהה על כך?).
</p>
<p>
ההתנגדות הבולטת והידועה ביותר למבחן טיורינג - ניסוי "<a href="http://he.wikipedia.org/wiki/%D7%94%D7%97%D7%93%D7%A8_%D7%94%D7%A1%D7%99%D7%A0%D7%99">החדר הסיני</a>" של סרל - נופלת, לדעתי, לקטגוריה הזו. החדר הסיני ראוי לפוסט משל עצמו, אם כי בשל אופיו הפילוסופי אני בספק אם אכתוב כזה, אבל אני ממליץ לכולכם לקרוא עליו. דעתי האישית היא שהניסוי לא אומר שום דבר על מבחן טיורינג, אבל לא אגן על הדעה הזו כרגע. אולי בתגובות.
</p>
</li>

<li>
<p>
טיעון חוסר-היכולות: זה עוד טיעון נפוץ ביותר בדיונים פופולריים. טיורינג מתאר אותו בקצרה כ"אוקי, מכונות יכולות לעשות את כל מה שתיארת, אבל הן לעולם לא יוכלו לעשות את X" כאשר X הוא, למשל, "להיות טובי לב, יצירתיים, יפים, חברותיים, בעלי יוזמה, חוש הומור, חוסר מוסרי, לעשות טעויות, להתאהב, להינות מתותים בקצפת, לגרום למישהו להתאהב בהם, ללמוד מנסיון, להשתמש במילים בצורה נכונה, לחשוב על עצמם, להתנהג בצורות מגוונות כמו אנשים, לעשות משהו באמת חדש".

</p>
<p>
טיורינג כותש את הטיעון הזה היטב. ראשית, כל הטענות לעיל הן <strong>חסרות ביסוס</strong>. בימינו כבר אפשר לומר במפורש בחלק מהמקרים הן פשוט נתגלו כלא נכונות (ווטסון, מישהו?), ואני לא מכיר אף טיעון משכנע לגבי האחרות מדוע הן נכונות באופן אבסולוטי. נכון, קשה לחשוב על מחשב שמתאהב; אבל זה בגלל שכשאנחנו חושבים על מחשבים, אנחנו חושבים על היצורים שיש לנו בכיס או על השולחן בבית. היצורים הללו, כבודם הרב במקומם מונח, אפילו לא <strong>מתחילים</strong> לדגדג את קצה הקרחון של הפוטנציאל של מכונות חישוב. זה בערך כמו לומר שבני אדם לא יכולים להתאהב כי ממבט חטוף באמבה אנחנו מקבלים את הרושם שהיא לא מסוגלת לכך.
</p>
</li>

<li>
<p>
הטיעון של עדה לבאלייס: זו בעצם הרחבה של אחד מטיעוני חוסר-היכולת הנפוצים ביותר. עדה לאבלייס הייתה שותפתו לעבודה של צ'ארלס בבאג', הממציא הבריטי בן המאה ה-19 שהקדים את זמנו במאה שנים בערך והמציא מחשב מכני - "המנוע האנליטי" - שבאופן מצער למדי לא הושלם מעולם וקצת נשכח (לא לגמרי, כפי שתעיד העובדה שטיורינג כותב עליו - עם זאת, דומני שטיורינג עוד לא הכיר את בבאג' כאשר כתב את המאמר שלו מ-1936 שבו המציא בעצמו את המחשב). לאבלייס כתבה את מה שניתן לתאר כ"תוכניות מחשב" עבור המחשב של בבאג', ולכן זכתה לתואר "המתכנתת הראשונה" (ושפת התכנות עדה נקראת על שמה).
</p>
<p>
טיורינג מצטט אמירה שלה - "המנוע האנליטי לא מתיימר לחדש שום דבר. הוא עושה את מה שאנו יודעים להורות לו כיצד לעשות". האמירה הזו, כמובן, תקפה גם למרבית תוכניות המחשב הקיימות כיום, אם כי אני כבר חש צורך להסתייג מלומר "בכולן".
</p>
<p>
הבעיה בטיעון הזה, כרגיל, היא שגם מחשב שפועל על פי תוכנית מחשב מדוקדקת שהכתבנו לו עדיין עשוי לעשות דברים שכלל לא חשבנו שיעשה, ולגלות דברים שאנחנו לא העלינו בדעתנו. אומר טיורינג, באחד מהציטוטים האהובים עלי ביותר שנוגעים למדעי המחשב -
</p>
<blockquote dir="ltr">The view that machines cannot give rise to surprises is due, I believe, to a fallacy to which philosophers and mathematicians are particularly subject. This is the assumption that as soon as a fact is presented to a mind all consequences of that fact spring into the mind simultaneously with it. It is a very useful assumption under many circumstances, but one too easily forgets that it is false. A natural consequence of doing so is that one then assumes that there is no virtue in the mere working out of consequences from data and general principles.</blockquote>
<p>
לי אישית קרה לא פעם ולא פעמיים שבמהלך בדיקה של דבר מה מתמטי כתבתי תוכנית מחשב פשוטה שתעזור לי בחיפושים, והיא מצאה דברים שאני בכלל לא העליתי בדעתי. וכאן מדובר על תוכניות מחשב אלמנטריות; תוכנית מחשב שתעבור את מבחן טיורינג תהיה כנראה מורכבת יותר בסדרי גודל רבים, ואני בספק אם היא תיכתב במלואה על ידי אדם.
</p>
</li>

<li>
<p>
הטיעון של רציפות מערכת העצבים: זה טיעון קצת יותר מחוכם מהטיעונים שהובאו עד כה, ופנרוז נוקט בוריאציה עליו, כמו גם אחרים. מחשב, וגם המודלים התיאורטיים הסטנדרטיים שלו, הם יצורים <strong>בדידים</strong>; דהיינו, אפשר לתאר את התנהגותם על ידי אוסף סופי של הנחיות סופיות (אני מאוד לא מדויק כאן, מתוך מטרה לא להפוך את הדיון לטכני מדי ולהסביר מה ההבדל בין "רציף" ו"בדיד" במתמטיקה). אם רוצים, אפשר גם להכניס דברים כמו אפקטים קוונטיים לתמונה (זה מה שפנרוז עושה), אם כי טיורינג לא מזכיר זאת. בשורה התחתונה זו ההנחה שיש בטבע משהו שהמודלים המתמטיים והמחשבים שבנויים לפיהם אינם ממדלים, ואולי החשיבה מסתתרת "שם".
</p>
<p>
לדעתי זה טיעון חזק, אולי הטיעון החזק ביותר - אבל לא נגד העקרון לפיו מכונות יכולות לחשוב, אלא רק נגד העקרון לפיו <strong>מחשבים כמו שאנו בונים אותם כיום</strong> מסוגלים לחשוב. הטיעון הזה עשוי להיות קונסטרוקטיבי במובן זה שהוא יצביע על האופן שבו צריך להרחיב את המודלים ואת האופנים שבהם אנו בונים מחשבים פיזיים כדי שיוכלו לחשוב.
</p>
<p>
טיורינג עצמו, בצורה אופטימית למדי, מניח שמכונות חישוב "רציפות" יהיו ניתנות לסימולציה <strong>מקורבת</strong> בעזרת מכונות חישוב "בדידות", ובתנאים של מבחן טיורינג, שבהם בסך הכל מעבירים הודעות סופיות בין המחשב והבוחן, לא תהיה לבוחן יכולת לשאול שאלות שיהיו מסוגלות להבדיל בין מכונת החישוב הרציפה ובין מכונת החישוב הבדידה. למיטב ידיעתי זה מצב העניינים גם כיום, אבל אני עצמי לא בטוח כל כך שזה לא ישתנה בעתיד. אולי.
</p>
</li>
<li>
<p>
הטיעון של ההתנהגות הלא-פורמלית: זה טיעון די חלש לדעתי ולכן לא ארחיב עליו יותר מדי. בקצרה, זהו הטיעון לפיו אי אפשר לתאר את ההתנהגות האנושית (נאמר, של אדם אחד ספציפי) באמצעות סט כלליים פורמליים, אבל כל תוכנית מחשב מתוארת כך. אני לא חושב שזה סותר בצורה כלשהי את הטענה שמחשב מסוגל לחשוב, ויותר מכך - אני לא מקבל את הטענה שאי אפשר לתאר את ההתנהגות האנושית באמצעות סט כללים פורמליים. גישה פיזיקלית רדוקציוניסטית תגיד ש<strong>אפשר</strong> לעשות בדיוק את זה. כמובן, זה שאפשר <strong>לנסח</strong> את הכללים לא אומר שיש לנו דרך להפיק מהם מידע <strong>בפועל</strong>, כי החישובים שיידרשו לצורך כך הם מסובכים מדי; אבל אל דאגה, אותו דבר תקף גם עבור מכונות חישוב (בהינתן סט הכללים הפורמליים שמגדירים מכונת חישוב מסויימת, אין לנו מושג איך לומר אפילו דברים פשוטים יחסית על התנהגותה - למשל, האם החישוב שלה יסתיים אי פעם או לא).
</p>
</li>

<li>
<p>
הטיעון של תפיסה על-חושית: כאן טיורינג הולך לכיוון הזוי למדי. אצטט את ההתחלה:
</p>
<blockquote dir="ltr">I assume that the reader is familiar with the idea of extrasensory perception, and the meaning of the four items of it, viz., telepathy, clairvoyance, precognition and psychokinesis. These disturbing phenomena seem to deny all our usual scientic ideas. How we should like to discredit them! Unfortunately the statistical evidence, at least for telepathy, is overwhelming</blockquote>
<p>
אין לי מושג על אילו ראיות סטטיסטיות טיורינג מדבר; למיטב ידיעתי, כל התופעות שהוא מדבר עליו מעולם לא הוכחו בצורה משכנעת דיו, ואת המתעניינים אפנה לבלוג "<a href="http://sharp-thinking.com/">חשיבה חדה</a>" שעוסק בדיוק בעניינים הללו. אפשר לסיים את הדיון כאן; עם זאת, אם אכן <strong>יש</strong> לאנשים יכולות טלפתיות זה ללא ספק יקשה על מחשב לעבור את המבחן גם אם הוא אכן חושב. מצד שני, למה שמחשב לא יהיה גם כן בעל יכולות טלפתיות? (וכמובן, לאסימוב יש סיפור <a href="http://en.wikipedia.org/wiki/Liar!">בדיוק על זה</a>).
</p>
</li>
</ul>

כאן מסתיים החלק הזה של המאמר. בחלק האחרון שלו טיורינג מנסה לנקוט בגישה חיובית ולתאר בקווים כלליים איך ייתכן שמחשב יעבור את המבחן. באופן טבעי, הוא לא מניח שמישהו יצליח לתכנת במו ידיו מחשב שעובר את המבחן, אלא שניתן יהיה לתכנת מחשב ש"לומד" ומתפתח. כיום אנחנו עדיין רחוקים ממחשבים כאלו (למרות תחום שלם שנקרא "למידה חישובית"), אבל אני סבור שאם אכן יהיו יום אחד מחשבים בעלי תודעה וחשיבה, זה יהיה האופן שבו הם יווצרו.

למרות שלא ברור לי עד כמה המאמר מוצלח בשכנוע מי שלא מחזיק כבר מראש בעמדות דומות לשל טיורינג, אני חושב שהוא מבהיר יפה את הבעיה, והמבחן שהוא מציע הוא דרך נחמדה להתמודד איתה. אם תרצו, סוג של אבן דרך שאם נעבור אותה, נדע בודאות שהשגנו פריצת דרך בכל הנוגע ליכולת החשיבה של מכונות. בימינו, מיותר לציין, אנחנו עדיין מאוד רחוקים מזה.

בימינו ישנה <a href="http://www.loebner.net/Prizef/loebner-prize.html">תחרות שנתית</a> של תוכנות מחשב שמנסות לנצח במבחן טיורינג. בינתיים עיקר האתגר הוא בביצועים של התוכנות אחת ביחס לשניה; אני ממליץ לכם להתבונן באתר התחרות אם זה מסקרן אתכם. עם זאת, ה"תחרות" האמיתית והמעניינת עוד יותר לדעתי מתקיימת בכל מקום ברשת האינטרנט. ישנם שירותים רבים שאינם מעוניינים לאפשר לתוכנות מחשב ("בוטים") לגשת אליהם (שכן זה מקל על פרסום זבל, פריצת חשבונות ושאר מריעין בישין) ולכן הם מנסים לאמת את העובדה שהפונה אליהם הוא אדם ולא מחשב. האמצעים שבהם הם משתמשים מהווים המחשה נאה לאופן שבו בוחן "עכשווי" במבחן טיורינג היה מגלה מיד שמדבר איתו מחשב. לרוב פשוט מציגים למשתמש תמונה ובה אותיות ומספרים שמוצגות בצורה מעוותת; המוח האנושי מסוגל לפענח יחסית בקלות את הג'יבריש (יחסית! כולנו נכשלנו לא פעם בדברים הללו!) בעוד שמחשבים מתקשים בכך יותר (אולם עצם העובדה שכל הזמן מחליפים את השיטות שבהן משתמשים מעידה על כך שמחשבים <strong>מצליחים</strong> להתמודד עם הבעיה הזו בהינתן אלגוריתם מתאים).

[caption id="attachment_2203" align="aligncenter" width="740"]<a href="{{site.baseurl}}{{site.post_images}}/2012/09/Suspicion.png"><img class="size-full wp-image-2203" title="Suspicion" src="{{site.baseurl}}{{site.post_images}}/2012/09/Suspicion.png" alt="" width="740" height="225" /></a> אל תשכחו להיבדק![/caption]

מקומות אחרים, למשל פורומים זניחים שאינם צריכים לחשוש מבוט שיהונדס ספציפית כדי לתקוף אותם, יכולים להשתמש בשיטה שהיא בו זמנית חזקה בהרבה אבל גם חלשה בהרבה - פשוט לשאול שאלה כלשהי בשפה טבעית שכולם יודעים את התשובה עליה. זו שיטה חלשה מאוד במובן זה שקל לבנות בוט שעונה נכון לשאלה, פשוט על ידי כך שנזין לו את התשובה כחלק מהתוכנית שלו; אבל קשה ביותר לבנות בוט שידע לפענח ולענות על כל השאלות. מצד שני, אולי זה בעצם אלמנטרי, ווטסון.