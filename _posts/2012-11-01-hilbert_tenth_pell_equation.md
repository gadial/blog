---
id: 2220
title: "הבעיה העשירית של הילברט - איך משוואת פל קשורה לכל העניין?"
date: 2012-11-01 06:54:56
layout: post
categories: 
  - תורת המספרים
tags: 
  - הבעיה העשירית של הילברט
  - טכני
  - משוואת פל
---
בואו נחזור לדבר על הבעיה העשירית של הילברט ש<a href="http://www.gadial.net/2012/09/15/hilbert_tenth_sequence_function/">עזבתי בשיא המתח</a> - בדיוק לפני החלק הטכני ביותר, שנתחיל לטפל בו הפעם. תזכורת קטנה למי שאין לו כוח לקרוא את הפוסטים הקודמים: המטרה שלנו היא להוכיח שהפונקציה {% equation %}f\left(n,k\right)=n^{k}{% endequation %} - "הפונקציה האקספוננציאלית" - היא דיופנטית. כלומר, שקיימת מערכת של משוואות פולינומיות בשלמים עם המון משתנים ששלושה מהם הם {% equation %}n,k,m{% endequation %} כך שלכל הצבה של ערכים ב-{% equation %}n,k,m{% endequation %}, יש פתרון למערכת המשוואות אם ורק אם {% equation %}m=n^{k}{% endequation %}. אפשר, כמובן, להתחיל מלהציג את מערכת המשוואות הזו, אבל היא כוללת שתיים-עשרה משוואות ולא מעט משתנים וממבט ראשון לא יהיה ברור מה הולך שם בכלל, אז נחכה עם זה קצת בסבלנות. לפני כן נטפל בבעיה לכאורה לא קשורה, אבל כזו שתוביל אותנו כמעט ישירות אל הפונקציה האקספוננציאלית: <a href="http://www.gadial.net/2012/08/31/pell_equation/">משוואת פל</a>.

כחלק מההכנה לפוסט הזה כתבתי פוסט על משוואת פל שאין צורך לחזור על כל מה שנאמר בו (מרטין דיוויס, במאמר על הבעיה העשירית של הילברט שאני מתבסס עליו, מוכיח מאפס את התכונות שהוא צריך באופן ישיר), אבל בואו נחזור על עיקרי הדברים הרלוונטיים. אם {% equation %}d{% endequation %} הוא מספר טבעי שאינו ריבוע, אז משוואת פל עם הפרמטר {% equation %}d{% endequation %} היא המשוואה {% equation %}x^{2}-dy^{2}=1{% endequation %} (בפוסט שלי השתמשתי ב-{% equation %}N{% endequation %} אבל עכשיו אני הולך לפי סגנון הכתיבה של דיוויס). מה שמעניין במשוואת פל הוא שלפתרונות שלה יש <strong>מבנה</strong> יפה במיוחד: קיים פתרון אחד שנקרא <strong>הפתרון היסודי</strong> ונסמן אותו בתור {% equation %}\left(x_{1},y_{1}\right){% endequation %}, כך שכל פתרון אחד מתקבל כמעין חזקה של הפתרון היסודי.

ליתר דיוק, מה שעושים הוא להסתכל על המספר האלגברי {% equation %}x_{1}+\sqrt{d}y_{1}{% endequation %} ולקחת את החזקות שלו, כלומר מגדירים {% equation %}x_{n}+\sqrt{d}y_{n}=\left(x_{1}+\sqrt{d}y_{1}\right)^{n}{% endequation %}. למי שאין לו כוח להתעסק עם שורשים אפשר לעשות את זה גם באופן ישיר בצורה הבאה: אם {% equation %}\left(x_{n},y_{n}\right){% endequation %} ו-{% equation %}\left(x_{k},y_{k}\right){% endequation %} הם שני פתרונות של משוואת פל, אז אפשר לבנות מהם על ידי "כפל" פתרון חדש {% equation %}\left(x_{t},y_{t}\right){% endequation %} שנראה כך:

{% equation %}x_{t}=x_{n}x_{k}+dy_{n}y_{k}{% endequation %}

{% equation %}y_{t}=x_{n}y_{k}+x_{k}y_{n}{% endequation %}

זוכרים משהו מזה? יפה. לא זוכרים? לא נורא, זה מה שצריך לזכור. בואו נעבור למה שדיוויס עושה. ראשית כל, <strong>למה</strong> הוא בכלל מתעניין במשוואת פל? ובכן, מצד אחד זו משוואה דיופנטית פשוטה - תנאי כמו {% equation %}x^{2}-dy^{2}=1{% endequation %} אפשר לקודד עם האמצעים שמותר לנו להשתמש בהם. מצד שני, הקטע הזה של "כל פתרון הוא חזקה של הפתרון היסודי" מתנהג כמו, ובכן, חזקה. זהו ה"גשר" שאנו זקוקים לו בין משהו דיופנטי ומשהו אקספוננציאלי. לדעתי זה די מגניב שזה נעשה באמצעות משוואת פל.

בשביל הצרכים שלו, דיוויס נזקק רק למשוואות פל מסוג מסויים: משוואות מהצורה {% equation %}x^{2}-dy^{2}=1{% endequation %} (עד כאן הכל כרגיל) כך ש-{% equation %}d=a^{2}-1{% endequation %}, עבור {% equation %}a&gt;1{% endequation %} כלשהו. כלומר, המשוואות {% equation %}x^{2}-3y^{2}=1{% endequation %}, {% equation %}x^{2}-8y^{2}=1{% endequation %}, {% equation %}x^{2}-15y^{2}=1{% endequation %} וכדומה (כזכור, אם {% equation %}d{% endequation %} הוא ריבוע "ממש", כלומר אם {% equation %}d=a^{2}{% endequation %}, אז למשוואה אין פתרונות) למשוואות שבהן {% equation %}d=a^{2}-1{% endequation %} קל מאוד לתת פתרון: {% equation %}x=a,y=1{% endequation %} תמיד פותר את המשוואה, שהרי {% equation %}a^{2}-\left(a^{2}-1\right)1^{2}=a^{2}-a^{2}+1=1{% endequation %}. האם זהו הפתרון היסודי, כלומר הפתרון שבעזרת "חזקות" שלו (ביחס לפעולת ה"כפל" שהצגתי למעלה) אפשר לקבל את כל שאר הפתרונות הלא טריוויאליים של המשוואה?

כדי להוכיח את זה מספיק להוכיח שאם {% equation %}\left(x,y\right){% endequation %} הוא פתרון כלשהו של המשוואה, אז לא ייתכן שמתקיים {% equation %}1&lt;x+y\sqrt{d}&lt;a+\sqrt{d}{% endequation %}, כלמר אין פתרון למשוואה "בין" שני הפתרונות הבסיסיים {% equation %}\left(1,0\right){% endequation %} ו-{% equation %}\left(a,1\right){% endequation %}. זה מספיק כי אם {% equation %}a+\sqrt{d}&lt;x+y\sqrt{d}{% endequation %}, אז בוודאי שגם {% equation %}a+\sqrt{d}&lt;\left(x^{2}+dy^{2}\right)+\left(xy+yx\right){% endequation %}, כלומר החזקה השניה של הפתרון {% equation %}\left(x,y\right){% endequation %} לא יכולה לתת את {% equation %}\left(a,1\right){% endequation %}, וגם החזקה השלישית וכן הלאה, מה שמאלץ את {% equation %}\left(a,1\right){% endequation %} להיות הפתרון היסודי.

אם כן, בואו נניח בכשלילה ש-{% equation %}\left(x,y\right){% endequation %} הוא פתרון של המשוואה שגם מקיים {% equation %}1&lt;x+y\sqrt{d}&lt;a+\sqrt{d}{% endequation %}. כעת, מכיוון שמתקיים {% equation %}x^{2}-dy^{2}=1{% endequation %} הרי שאפשר לפרק את הביטוי הזה ולקבל

{% equation %}\left(x-y\sqrt{d}\right)\left(x+y\sqrt{d}\right)=x^{2}-dy^{2}=1=a^{2}-d=\left(a-\sqrt{d}\right)\left(a+\sqrt{d}\right){% endequation %}

בואו נחלק את שני האגפים ב-{% equation %}x+y\sqrt{d}{% endequation %}. נקבל:

{% equation %}x-y\sqrt{d}=a-\sqrt{d}\cdot\frac{a+\sqrt{d}}{x+y\sqrt{d}}&gt;a-\sqrt{d}{% endequation %}

כי הרי הביטוי {% equation %}\frac{a+\sqrt{d}}{x+y\sqrt{d}}{% endequation %} הוא גדול מ-1 אם מניחים ש-{% equation %}x+y\sqrt{d}&lt;a+\sqrt{d}{% endequation %}. עכשיו, נכפול את שני האגפים במינוס 1, הסימן של אי השוויון יתהפך ולבסוף נקבל:

{% equation %}-x+y\sqrt{d}&lt;-a+\sqrt{d}{% endequation %}

אם נחבר את זה לאי השוויון {% equation %}x+y\sqrt{d}&lt;a+\sqrt{d}{% endequation %} נקבל בסופו של דבר ש-{% equation %}2y\sqrt{d}&lt;2\sqrt{d}{% endequation %}, כלומר {% equation %}y&lt;1{% endequation %}. זה לכשעצמו עדיין לגיטימי - אולי {% equation %}y{% endequation %} שלילי, או אפס? לכן אנו נזקקים לעוד תעלול. נשים לב לכך שעל פי הנחתנו, {% equation %}x+y\sqrt{d}&gt;1{% endequation %} ולכן {% equation %}\left(x-y\sqrt{d}\right)=\frac{1}{x+y\sqrt{d}}&lt;1{% endequation %}, ולכן {% equation %}-x+y\sqrt{d}&gt;-1{% endequation %}, ואם נחבר את זה ל-{% equation %}1&lt;x+y\sqrt{d}{% endequation %} נקבל ש-{% equation %}0&lt;y{% endequation %}, כלומר {% equation %}0&lt;y&lt;1{% endequation %}, כלומר {% equation %}y{% endequation %} בכלל לא מספר שלם, אבל רק מספרים שלמים הם פתרונות חוקיים של משוואת פל. זה מסיים את הסיפור. אני מודה, ההוכחה הזו היא לא הדבר הכי יפה בעולם.

עכשיו, משאנחנו יודעים מהו הפתרון היסודי, אפשר לתת סימון כללי לשאר הפתרונות החיוביים. מכיוון שהמשוואה שלנו תלויה גם ב-{% equation %}d{% endequation %}, אבל את {% equation %}d{% endequation %} כתבנו בתור {% equation %}a^{2}-1{% endequation %}, אנחנו משתמשים ב-{% equation %}x_{n}\left(a\right){% endequation %} ו-{% equation %}y_{n}\left(a\right){% endequation %} כדי לתאר את הפתרונות. פורמלית הסדרות הללו מוגדרות כך: {% equation %}x_{0}\left(a\right)=1,y_{0}\left(a\right)=0{% endequation %}, ובאופן אינדוקטיבי:

{% equation %}x_{n+1}\left(a\right)=ax_{n}\left(a\right)+dy_{n}\left(a\right){% endequation %}

{% equation %}y_{n+1}\left(a\right)=ay_{n}\left(a\right)+x_{n}\left(a\right){% endequation %}

או בצורה טיפה יותר אלגנטית אבל לא מפורשת, {% equation %}x_{n}\left(a\right)+y_{n}\left(a\right)\sqrt{d}=\left(a+\sqrt{d}\right)^{n}{% endequation %}. אבחנה חביבה של דיוויס בנקודה הזו היא שהנוסחה הזו דומה באופיה לנוסחת אוילר, {% equation %}\cos\theta+i\sin\theta=e^{i\theta}{% endequation %}. כאן {% equation %}\cos{% endequation %} מיוצג על ידי {% equation %}x_{n}\left(a\right){% endequation %}, {% equation %}\sin{% endequation %} מיוצג על ידי {% equation %}y_{n}\left(a\right){% endequation %}, במקום {% equation %}i{% endequation %} יש לנו את {% equation %}\sqrt{d}{% endequation %} ובמקום {% equation %}e^{i}{% endequation %} יש לנו את {% equation %}a+\sqrt{d}{% endequation %}. דיוויס מצביע על כך שניתן להשתמש בייצוג המעריכי הזה כדי לקבל בקלות נוסחאות לחיבור וחיסור (למעשה, כבר יש לנו את הנוסחה לחיבור...) שמזכירות את הנוסחאות המקבילות מטריגו - ושוב, לא במקרה! הדרך הכי טובה לפתח את הנוסחאות מטריגו היא לעבור דרך נוסחת אוילר שפשוט נותנת לנו אותן במתנה. אני מציע לכם לשחק קצת עם המשוואות ולהוכיח את הנוסחאות הללו לעצמכם בדרך הזו:

{% equation %}x_{m\pm n}=x_{m}x_{n}\pm dy_{m}y_{n}{% endequation %}

{% equation %}y_{m\pm n}=x_{n}y_{m}\pm x_{m}y_{n}{% endequation %}

שימו לב שכבר התעצלתי מלכתוב את ה-{% equation %}\left(a\right){% endequation %} אחרי ה-{% equation %}x_{n},y_{n}{% endequation %} וכך גם אמשיך לעשות בהמשך אם זהותו המדויקת של ה-{% equation %}a{% endequation %} לא רלוונטית באותו רגע או ברורה מההקשר.

עכשיו בואו ננסה להבין כמה תכונות תורת-מספריות של הפתרונות הללו שיהיו חשובות בהמשך. <strong>אני מזהיר מראש</strong> - מכאן ועד סוף הפוסט לא תהיה שום תובנה מהותית לגבי מה לעזאל הולך כאן. רק אוסף של הרבה תכונות, כולן פשוטות בפני עצמן, שבהן נשתמש בצורה אינטנסיבית בפוסט הבא, שבו סוף סוף נדבר על איך מוכיחים שהפונקציה האקספוננציאלית היא דיופנטית. אתם יכולים לדלג על המשך הפוסט אלא אם אתם רוצים (כמוני) לוודא שאתם מבינים את כל מה שהולך בהוכחה הזו.

בתור התחלה, {% equation %}x_{n},y_{n}{% endequation %} הם <strong>זרים</strong> - אין להם מחלק משותף חיובי גדול מ-1. זה מסומן בתור {% equation %}\left(x_{n},y_{n}\right)=1{% endequation %}. למה? פשוט: אם {% equation %}d{% endequation %} חיובי מחלק את {% equation %}x_{n}{% endequation %} ואת {% equation %}y_{n}{% endequation %} אז הוא בוודאי מחלק גם את {% equation %}x_{n}^{2}{% endequation %} ואת {% equation %}dy_{n}^{2}{% endequation %} ולכן גם מחלק את ההפרש ביניהם, שהוא 1. אם {% equation %}d{% endequation %}הוא חיובי ומחלק את 1, הוא בהכרח 1 בעצמו.

קצת יותר מעניינת הטענה ש-{% equation %}y_{n}{% endequation %} מחלק את {% equation %}y_{nk}{% endequation %}. זה מן הסתם נכון עבור {% equation %}k=1{% endequation %} אבל לערכים גדולים יותר יש צורך להוכיח זאת באינדוקציה, בעזרת נוסחת החיבור שלנו:

{% equation %}y_{n\left(k+1\right)}=y_{nk+n}=x_{n}y_{nk}+x_{nk}y_{n}{% endequation %}

מהנחת האינדוקציה עולה ש-{% equation %}y_{n}{% endequation %} מחלק את {% equation %}y_{nk}{% endequation %} ולכן את {% equation %}x_{n}y_{nk}{% endequation %}, וברור שהוא מחלק את {% equation %}x_{nk}y_{n}{% endequation %}, ולכן קיבלנו ש-{% equation %}y_{n}{% endequation %} מחלק את {% equation %}y_{n\left(k+1\right)}{% endequation %}. האם יש עוד איברים בסדרת ה-{% equation %}y{% endequation %}-ים אותם {% equation %}y_{n}{% endequation %} יכול לחלק? מסתבר שלא. נניח ש-{% equation %}y_{n}{% endequation %} מחלק את {% equation %}y_{t}{% endequation %} אבל {% equation %}n{% endequation %} לא מחלק את {% equation %}t{% endequation %}. אז אפשר לחלק אותם עם שארית, כלומר לכתוב {% equation %}t=qn+r{% endequation %} כאשר {% equation %}0&lt;r&lt;n{% endequation %} היא השארית. נקבל: {% equation %}y_{t}=x_{r}y_{nq}+x_{nq}y_{r}{% endequation %}. אם {% equation %}y_{n}{% endequation %} מחלק את הביטוי הזה, אז מכיוון שאנו יודעים שהוא מחלק את {% equation %}y_{nq}{% endequation %} נקבל שהוא חייב לחלק את {% equation %}x_{nq}y_{r}{% endequation %}. כעת, {% equation %}\left(y_{nq},x_{nq}\right)=1{% endequation %} ולכן לא ייתכן ש-{% equation %}y_{n}{% endequation %} יחלק את {% equation %}x_{nq}{% endequation %}, אחרת הוא היה גורם משותף שלו ושל {% equation %}y_{nq}{% endequation %}. לכן בהכרח {% equation %}y_{n}{% endequation %} מחלק את {% equation %}y_{r}{% endequation %}, אבל זה בלתי אפשרי כי {% equation %}y_{n}&gt;y_{r}{% endequation %}! סוף הסיפור.

אתם בוודאי תוהים לאן אני חותר עם כל התכונות הללו. המטרה היא למצוא משהו שאפשר לקודד דיופנטית איכשהו ויאפשר לנו לאפיין את הסדרות {% equation %}x_{n},y_{n}{% endequation %} במדויק. הכיוון המבטיח ביותר הוא תכונות של הסדרות הללו מודולו משהו. כזכור, {% equation %}a\equiv_{n}b{% endequation %} פירושו ש-{% equation %}n{% endequation %} מחלק את {% equation %}a-b{% endequation %} (ובמילים אחרות, שהשארית של חלוקת {% equation %}a{% endequation %} ו-{% equation %}b{% endequation %} ב-{% equation %}n{% endequation %} היא זהה). הנה דוגמה ראשונה לתכונת מודולו:

{% equation %}y_{nk}\equiv_{y_{n}^{3}}kx_{n}^{k-1}y_{n}{% endequation %}

טוב, במבט ראשון המשוואה הזו נראית מונפצת לגמרי. איך בכלל הגיעו אליה? התשובה היא שמישהו כנראה ניסה, על מנת להבין את הסדרות {% equation %}x_{n},y_{n}{% endequation %}, לשחק איתן כמה שיותר. הוא כנראה הסתכל על האיבר {% equation %}x_{nk}+y_{nk}\sqrt{d}=\left(x_{n}+y_{n}\sqrt{d}\right)^{k}{% endequation %} ושאל את עצמו - הממ, מה יקרה אם פשוט נפתח את הסוגריים באמצעות הבינום של ניוטון (הדרך ה"רגילה" לפתוח סוגריים שכאלה)? התשובה היא שנקבל:

{% equation %}\left(x_{n}+y_{n}\sqrt{d}\right)^{k}=\sum_{i=0}^{k}{k \choose i}x_{n}^{k-i}\left(y_{n}\sqrt{d}\right)^{i}=\sum_{i=0}^{k}{k \choose i}x_{n}^{k-i}y_{n}^{i}d^{\frac{i}{2}}{% endequation %}

שימו לב ל-{% equation %}d^{\frac{i}{2}}{% endequation %}. עבור הערכים הזוגיים של {% equation %}i{% endequation %} זהו מספר טבעי, ולכן כל הגורם {% equation %}{k \choose i}x_{n}^{k-i}y_{n}^{i}d^{\frac{i}{2}}{% endequation %} יתרום ל-{% equation %}x_{nk}{% endequation %} במקרה הזה. עבור {% equation %}i{% endequation %} אי זוגי נקבל {% equation %}\sqrt{d}{% endequation %} בחזקת משהו אי זוגי, ולכן כל הגורם יתרום ל-{% equation %}y_{nk}\sqrt{d}{% endequation %}. אם נחלק ב-{% equation %}\sqrt{d}{% endequation %} את שני האגפים נקבל שהגורם הזה תורם {% equation %}{k \choose i}x_{n}^{k-i}y_{n}^{i}d^{\frac{i-1}{2}}{% endequation %} ל-{% equation %}y_{nk}{% endequation %}. לכן קיבלנו:

{% equation %}y_{nk}=\sum_{\begin{array}{c}i=1\\i\mbox{ odd}\end{array}}^{k}{k \choose i}x_{n}^{k-i}y_{n}^{i}d^{\frac{i-1}{2}}{% endequation %}

עכשיו משתמשים בתעלול שמשתמשים בו כל הזמן בתורת המספרים (תצטרכו להאמין לי). שמים לב לכך שפרט לאיבר הראשון בסכום, זה שמתקבל עבור {% equation %}i=1{% endequation %}, עבור כל שאר האיברים מתקיים {% equation %}i\ge3{% endequation %} ולכן {% equation %}y_{n}^{3}{% endequation %} מחלק את כולם, ולכן מודולו {% equation %}y_{n}^{3}{% endequation %} הם נעלמים (זו הסיבה שבגללה בוחרים {% equation %}y_{n}^{3}{% endequation %} דווקא - כדי שהמודולוס יהיה גדול יחסית ועדיין יישאר לנו ביטוי פשוט יחסית. לכן נישאר רק עם האיבר הראשון:

{% equation %}y_{nk}\equiv_{y_{n}^{3}}{k \choose 1}x_{n}^{k-1}y_{n}=kx_{n}^{k-1}y_{n}{% endequation %}

פתאום הביטוי הזה כבר לא נראה מפחיד כל כך. לפחות לא בשבילי. כמובן, עדיין לא ברור בשביל מה הוא טוב. אז הנה המסקנה המיידית שלו: מה קורה אם במשוואה שקיבלנו נציב {% equation %}k=y_{n}{% endequation %}? נקבל מייד

{% equation %}y_{ny_{n}}\equiv_{y_{n}^{3}}y_{n}x_{n}^{y_{n}-1}y_{n}=y_{n}^{2}x_{n}^{y_{n}-1}{% endequation %}

שזה אומר, בצורה הכי מפורשת שרק אפשר, ש-{% equation %}y_{ny_{n}}-y_{n}^{2}x_{n}^{y_{n}-1}=\alpha\cdot y_{n}^{3}{% endequation %}, כאשר {% equation %}\alpha{% endequation %} הוא מספר שלם לא מעניין כלשהו. נעביר אגפים, נוציא גורם משותף, ונקבל:

{% equation %}y_{ny_{n}}=y_{n}^{2}\left(x_{n}^{y_{n}-1}+\alpha y_{n}\right){% endequation %}

כלומר, המסקנה שלנו היא ש-{% equation %}y_{n}^{2}{% endequation %} מחלק את {% equation %}y_{ny_{n}}{% endequation %}. עוד תכונת התחלקות של הסדרה {% equation %}y_{n}{% endequation %}! כמו בתכונת ההתחלקות הקודמת, אנחנו גם רוצים להבין מה קורה בכיוון ההפוך. כלומר, אם {% equation %}y_{n}^{2}{% endequation %} מחלק {% equation %}y_{t}{% endequation %} כלשהו, אז מה אפשר לדעת על {% equation %}t{% endequation %}? במקרה שלנו אפשר להוכיח שבהכרח {% equation %}y_{n}{% endequation %} מחלק את {% equation %}t{% endequation %}. למה? טוב, ראשית, אם {% equation %}y_{n}^{2}{% endequation %} מחלק את {% equation %}y_{t}{% endequation %} אז בוודאי שגם {% equation %}y_{n}{% endequation %} מחלק אותו, וכבר ראינו שזה גורר ש-{% equation %}n{% endequation %} מחלק את {% equation %}t{% endequation %}, כלומר אפשר לכתוב {% equation %}t=nk{% endequation %}. עכשיו, {% equation %}y_{t}=y_{nk}\equiv_{y_{n}^{3}}kx_{n}^{k-1}y_{n}{% endequation %}, ולכן בגלל ש-{% equation %}y_{n}^{2}{% endequation %} מחלק את {% equation %}y_{t}{% endequation %} נקבל שהוא מחלק גם את {% equation %}kx_{n}^{k-1}y_{n}{% endequation %}, כלומר {% equation %}y_{n}{% endequation %} מחלק את {% equation %}kx_{n}^{k-1}{% endequation %}. כמו כן, {% equation %}\left(y_{n},x_{n}\right)=1{% endequation %} ולכן {% equation %}y_{n}{% endequation %} מחלק את {% equation %}k{% endequation %}, אבל {% equation %}t=nk{% endequation %} ולכן {% equation %}y_{n}{% endequation %} מחלק את {% equation %}t{% endequation %} - סיימנו.

לעצור. לנשום עמוק. אני כרגע יכול לראות רק "מחלק... מחלק... מחלק..." בכל מקום. זה לא שמשהו עד כה היה מסובך במיוחד אבל זה ים של פרטים שלא ברור עדיין לאן הם מובילים. קצת סבלנות ונגיע.

בואו נעבור לדבר עכשיו על משהו קצת שונה שקשור לסדרות {% equation %}x_{n},y_{n}{% endequation %} - אפשר להציג אותן גם באמצעות נוסחת נסיגה. בפרט:

{% equation %}x_{n+1}=2ax_{n}-x_{n-1}{% endequation %}

{% equation %}y_{n+1}=2ay_{n}-y_{n-1}{% endequation %}

ההוכחה כמעט מיידית באמצעות הנוסחאות שלנו ל-{% equation %}x_{n\pm m}{% endequation %} ו-{% equation %}y_{n\pm m}{% endequation %} ואתם מוזמנים לנסות ולמצוא אותה בעצמכם.

מה שנחמד בנוסחאות הנסיגה הללו הוא שהן מאפשרות להוכיח טענות על הסדרות {% equation %}x_{n},y_{n}{% endequation %} אינדוקטיבית. למשל, בואו נוכיח ש-{% equation %}y_{n}\equiv_{a-1}n{% endequation %}: ראשית כל בודקים ישירות שזה מתקיים עבור {% equation %}n=0,1{% endequation %}, ושנית:

{% equation %}y_{n+1}=2ay_{n}-y_{n-1}\equiv_{a-1}2n-\left(n-1\right)=n+1{% endequation %} (השתמשתי כאן בכך ש-{% equation %}a\equiv_{a-1}1{% endequation %})

כמו כן, וזה כבר מעניין למדי, אם {% equation %}a\equiv_{c}b{% endequation %} אז לכל {% equation %}n{% endequation %} מתקיים ש-{% equation %}x_{n}\left(a\right)\equiv_{c}x_{n}\left(b\right){% endequation %} ו-{% equation %}y_{n}\left(a\right)\equiv_{c}y_{n}\left(b\right){% endequation %}. גם ההוכחה פה היא מיידית מתוך נוסחת הנסיגה, כאשר המקרים {% equation %}n=0,1{% endequation %}טריוויאליים (מבחן - היכן אנו משתמשים שם בכך ש-{% equation %}a\equiv_{c}b{% endequation %}?). בכל הנוגע לצעד:

{% equation %}y_{n+1}\left(a\right)=2ay_{n}\left(a\right)-y_{n-1}\left(a\right)\equiv_{c}2by_{n}\left(b\right)-y_{n-1}\left(b\right)=y_{n+1}\left(b\right){% endequation %}

ואותו דבר בדיוק עבור {% equation %}x_{n}{% endequation %}.

עוד שעשוע הוא להיווכח בכך ש-{% equation %}y_{n}{% endequation %} הוא זוגי עבור {% equation %}n{% endequation %} זוגי, ואי זוגי עבור {% equation %}n{% endequation %} אי זוגי. את זה אפשר להסיק מהסתכלות על נוסחת הנסיגה מודולו 2:

{% equation %}y_{n+1}=2ay_{n}-y_{n-1}\equiv_{2}y_{n-1}{% endequation %}

ובגלל ש-{% equation %}y_{0}{% endequation %} זוגי ו-{% equation %}y_{1}{% endequation %} אי זוגי התוצאה נובעת.

רוצים עוד משהו? לא? ובכן, אין לכם ברירה. התוצאה הבאה היא באמת משהו שנראה הזוי לחלוטין ממבט ראשון ולא ברור מאיפה זה הגיע (ועד לשלב מתקדם יותר גם לא נבין מה עושים עם זה):

{% equation %}x_{n}\left(a\right)-y_{n}\left(a\right)\left(a-y\right)\equiv_{2ay-y^{2}-1}y^{n}{% endequation %}

מי זה {% equation %}y{% endequation %}? מספר כלשהו. אז למה דווקא לסמן אותו ב-{% equation %}y{% endequation %}? כדי לדבוק בסימונים של דיוויס.

ההוכחה, כרגיל, דורשת קודם כל לבדוק את המקרה של {% equation %}n=0,1{% endequation %}. בואו נעשה את זה במפורש הפעם:

{% equation %}x_{0}\left(a\right)-y_{0}\left(a\right)\left(a-y\right)=1-0\left(a-y\right)=1\equiv_{2ay-y^{2}-1}y^{0}{% endequation %}

{% equation %}x_{1}\left(a\right)-y_{1}\left(a\right)\left(a-y\right)=a-1\left(a-y\right)=y\equiv_{2ay-y^{2}-1}y^{1}{% endequation %}

ועכשיו נמשיך אינדוקטיבית:

{% equation %}x_{n+1}\left(a\right)-y_{n+1}\left(a\right)\left(a-y\right)=2a\left[x_{n}\left(a\right)-y_{n}\left(a-y\right)\right]-\left[x_{n-1}\left(a\right)-y_{n-1}\left(a-y\right)\right]\equiv_{2ay-y^{2}-1}2ay^{n}-y^{n-1}{% endequation %}

עוד לא סיימנו:

{% equation %}2ay^{n}-y^{n-1}=y^{n-1}\left(2ay-1\right)\equiv_{2ay-y^{2}-1}y^{n-1}y^{2}=y^{n+1}{% endequation %}

לב העניין כאן הוא המעבר {% equation %}\left(2ay-1\right)\equiv_{2ay-y^{2}-1}y^{2}{% endequation %} - ודאו שאתם מבינים למה הוא נכון.

עכשיו בואו נבין משהו על קצב הגידול של {% equation %}x_{n},y_{n}{% endequation %}. נתחיל מ-{% equation %}y_{n}{% endequation %}. כזכור, {% equation %}y_{n+1}=y_{n}x_{1}+y_{1}x_{n}=ay_{n}+x_{n}{% endequation %}, ולכן {% equation %}y_{n+1}&gt;ay_{n}{% endequation %} - בפרט אפשר להסיק ש-{% equation %}y_{n}{% endequation %} חיובי לכל {% equation %}n{% endequation %} (לא נצטרך יותר מזה).

בכל הנוגע ל-{% equation %}x_{n}{% endequation %}, יש לנו את הנוסחה {% equation %}x_{n+1}=x_{n}x_{1}+dy_{n}y_{1}=ax_{n}+dy_{n}{% endequation %}. אז {% equation %}x_{n+1}&gt;ax_{n}{% endequation %} לכל {% equation %}n{% endequation %}, ולכן אפשר להראות באינדוקציה ש-{% equation %}x_{n}\ge a^{n}{% endequation %}, כלומר הסדרה גדלה בקצב שהוא לפחות אקספוננציאלי. זה חסם מלמטה, אבל האם אפשר לחסום גם מלמעלה? ובכן, בקלות, עם נוסחת הנסיגה של {% equation %}x_{n}{% endequation %}: {% equation %}x_{n+1}=2ax_{n}-x_{n-1}\le2ax_{n}{% endequation %} ולכן {% equation %}x_{n}\le\left(2a\right)^{n}{% endequation %}.

עוד טיפה וסיימנו. התכונה הבאה נראית מוזר למדי במבט ראשון:

{% equation %}x_{2n\pm i}\equiv_{x_{n}}-x_{i}{% endequation %}

אין כאן יותר מאשר שימוש בהגדרה:

{% equation %}x_{2n\pm i}=x_{n}x_{n\pm i}+dy_{n}y_{n\pm i}\equiv_{x_{n}}dy_{n}\left(y_{n}x_{i}\pm x_{n}y_{i}\right)\equiv_{x_{n}}dy_{n}^{2}x_{i}=\left(x_{n}^{2}-1\right)x_{i}\equiv_{x_{n}}-x_{i}{% endequation %}

כאן השתמשנו בכך ש-{% equation %}x_{n}^{2}-dy_{n}^{2}=1{% endequation %}, ולכן {% equation %}dy_{n}^{2}=x_{n}^{2}-1{% endequation %}.

מסקנה מיידית היא ש-{% equation %}x_{4n\pm i}\equiv_{x_{n}}x_{i}{% endequation %}, כי {% equation %}x_{4n\pm i}=x_{2n+\left(2n\pm i\right)}\equiv_{x_{n}}-x_{2n\pm i}\equiv_{x_{n}}x_{i}{% endequation %}.

עכשיו לתוצאה שההוכחה שלה תהיה טיפה יותר ארוכה, אבל כבר נראית די מעניינת: אם {% equation %}x_{i}\equiv_{x_{n}}x_{j}{% endequation %} כך ש-{% equation %}i\le j\le2n{% endequation %} ו-{% equation %}n&gt;0{% endequation %} אז {% equation %}i=j{% endequation %} למעט המקרה {% equation %}a=2,n=1,i=0,j=2{% endequation %}. זה מעניין כי זה מראה שאפשר לזהות בצורה ייחודית, בערך, איברים ב-{% equation %}x_{n}\left(a\right){% endequation %} על פי תכונות התחלקות שלהם, וזה משהו שאפשר לקודד דיופנטית, בערך.

בדרך כלל כשמדברים על חישובים מודולו {% equation %}n{% endequation %} (ל-{% equation %}n{% endequation %} כלשהו) אנו מסתכלים על הקבוצה {% equation %}\left\{ 0,1,2,\dots,n-1\right\} {% endequation %} ועושים בה את החשבון. אבל בתיאוריה יכלנו לעבוד גם עם הקבוצה {% equation %}\left\{ -1,0,\dots,n-2\right\} {% endequation %} או עם הרבה קבוצות אחרות - העיקר הוא רק למצוא קבוצה שבה אין שני מספרים ששקולים מודולו {% equation %}n{% endequation %}, ויש נציג לכל מחלקת שקילות מודולו {% equation %}n{% endequation %} (בניסוח פשוט, לכל מספר בין {% equation %}0{% endequation %} ל-{% equation %}n-1{% endequation %} יש בקבוצה איבר ששקול לו מודולו {% equation %}n{% endequation %}). בתורת המספרים לעתים מאוד נוח לעבוד עם קבוצת נציגים שאיננה {% equation %}\left\{ 0,1,\dots,n-1\right\} {% endequation %} אלא כוללת בחציה מספרים שליליים, כאילו הזזנו את הקבוצה {% equation %}\left\{ 0,1,\dots,n-1\right\} {% endequation %} מרחק של חצי {% equation %}n{% endequation %} בערך. כאשר {% equation %}n{% endequation %} אי זוגי אין כזה דבר, "חצי {% equation %}n{% endequation %}", אבל אפשר לדבר על המספר {% equation %}q=\frac{n-1}{2}{% endequation %} שהוא מספר שלם, ואז להתבונן על קבוצת הנציגים {% equation %}\left\{ -q,-q+1,\dots,-1,0,1,\dots,q\right\} {% endequation %} שכוללת בדיוק {% equation %}q{% endequation %} מספרים חיוביים, {% equation %}q{% endequation %} מספרים שליליים ואת {% equation %}0{% endequation %}, כלומר {% equation %}2q+1=n{% endequation %} מספרים, ומכיוון שהם כולם ברצף ההפרש בין אף זוג שלהם לא יכול להתחלק ב-{% equation %}n{% endequation %} (ההפרש המקסימלי הוא {% equation %}q-\left(-q\right)=2q=n-1{% endequation %}). כלומר, זו אכן קבוצת נציגים לגיטימית. כפי שאמרתי, לעתים נוח יותר לעבוד עם הקבוצה הזו וכך גם נעשה עכשיו.

אז בואו נניח ש-{% equation %}x_{n}{% endequation %} הוא אי זוגי וניקח את אוסף השאריות מ-{% equation %}-q{% endequation %} עד {% equation %}q{% endequation %} כאשר {% equation %}q=\frac{x_{n}-1}{2}{% endequation %}. עכשיו, בואו נסתכל לרגע במספרים {% equation %}x_{0},x_{1},x_{2},\dots,x_{n-1}{% endequation %}. ראשית, יש בדיוק {% equation %}n{% endequation %} כאלו. שנית, זו סדרה עולה: {% equation %}1=x_{0}&lt;x_{1}&lt;x_{2}&lt;\dots&lt;x_{n-1}&lt;x_{n}{% endequation %} וזאת בגלל נוסחת הנסיגה שמגדירה את ה-{% equation %}x_{n}{% endequation %}-ים. זה בפרט אומר שכל ה-{% equation %}x_{i}{% endequation %}-ים הללו שונים זה מזה מודולו {% equation %}x_{n}{% endequation %} (למה?). כעת, אפשר לחסום את הגודל של האיבר המקסימלי בסדרה: אנחנו יודעים ש-{% equation %}x_{n}=ax_{n-1}+dy_{n-1}\ge ax_{n-1}{% endequation %} ולכן {% equation %}x_{n-1}\le\frac{x_{n}}{a}\le\frac{x_{n}}{2}{% endequation %}. נובע מזה ש-{% equation %}x_{n-1}\le q{% endequation %} (כי {% equation %}x_{n-1}{% endequation %} הוא שלם ואילו {% equation %}q{% endequation %} הוא הערך השלם התחתון של {% equation %}\frac{x_{n}}{2}{% endequation %}). במילים אחרות, ה-{% equation %}x_{i}{% endequation %}-ים מתאימים <strong>לשאריות חיוביות</strong> בתוך הקבוצה {% equation %}\left\{ -q,-q+1,\dots,-1,0,1,\dots,q\right\} {% endequation %}.

בואו נסתכל עכשיו על המספרים ש<strong>מעבר</strong> ל-{% equation %}x_{n}{% endequation %}: {% equation %}x_{n+1},x_{n+2},\dots,x_{2n}{% endequation %}. לפני רגע ראינו את התכונה {% equation %}x_{2n\pm i}\equiv_{x_{n}}-x_{i}{% endequation %} ועכשיו היא תועיל לנו: היא אומרת שהסדרה {% equation %}x_{n+1},x_{n+2},\dots,x_{2n}{% endequation %} שקולה מודולו {% equation %}x_{n}{% endequation %} לסדרה {% equation %}-x_{n-1},-x_{n-2},\dots,-x_{0}{% endequation %}. מכיוון שה-{% equation %}x_{i}{% endequation %}-ים התאימו לשאריות חיוביות, זה אומר שה-{% equation %}x_{n+i}{% endequation %}-ים מתאימים לשאריות <strong>שליליות</strong> בתוך הקבוצה {% equation %}\left\{ -q,-q+1,\dots,-1,0,1,\dots,q\right\} {% endequation %}. השאריות החיוביות והשליליות בקבוצה לא שקולות זו לזו, ולכן קיבלנו שכל ה-{% equation %}x_{i}{% endequation %}-ים עד {% equation %}i\le2n{% endequation %} לא שקולים האחד לשני (אם אתם עדיין לא משוכנעים נסו להשלים את ההוכחה).

זה טיפל רק במקרה שבו {% equation %}x_{n}{% endequation %} אי זוגי. אם הוא זוגי אז נסמן {% equation %}q=\frac{x_{n}}{2}{% endequation %} ואוסף השאריות יהיה הפעם {% equation %}\left\{ -q+1,-q+1,\dots,-1,0,1,\dots,q\right\} {% endequation %}, כלומר הקצה השמאלי הוא לא {% equation %}-q{% endequation %} אלא מספר שגדול ממנו ב-1. מתי זה יכול להפריע להוכחה שלעיל? רק אם איכשהו הסדרה {% equation %}x_{i}{% endequation %} מגיעה אל {% equation %}q{% endequation %}, והיא יכולה להגיע רק באיבר האחרון שלה, כלומר {% equation %}x_{n-1}=q=\frac{x_{n}}{2}{% endequation %}. זה מקרה קצה, אבל זה עשוי להתרחש. אם זה התרחש, בואו נראה מה נוסחת הנסיגה של {% equation %}x_{n}{% endequation %} אומרת לנו:

{% equation %}x_{n}=ax_{n-1}+dy_{n-1}=a\frac{x_{n}}{2}+dy_{n-1}{% endequation %}

מתי זה יכול לקרות? מכיוון ש-{% equation %}a\ge2{% endequation %}, הדרך היחידה שבה נוכל לקבל שוויון היא אם {% equation %}a=2{% endequation %} (אחרת {% equation %}a\frac{x_{n}}{2}+dy_{n-1}&gt;x_{n}{% endequation %}), ובמקרה זה בהכרח {% equation %}y_{n-1}=0{% endequation %}, אבל זה קורה רק עבור {% equation %}n=1{% endequation %}. הנה הוכחנו שאנחנו במקרה הפרטי היחיד שסייגנו החוצה מראש בניסוח המשפט.

יפה, הוכחנו את המשפט, בואו נרחיב אותו טיפה ונראה שאם {% equation %}x_{i}\equiv_{x_{n}}x_{j}{% endequation %} תוך שאנו מאלצים את {% equation %}i{% endequation %} להיות קטן יותר - {% equation %}0&lt;i\le n{% endequation %} אבל מרשים ל-{% equation %}j{% endequation %} להיות גדול יותר - {% equation %}0\le j&lt;4n{% endequation %}, אז או ש-{% equation %}j=i{% endequation %} כמקודם או ש-{% equation %}j=4n-i{% endequation %}. ההוכחה פשוטה: אם {% equation %}j\le2n{% endequation %} פשוט נשתמש במשפט שזה עתה הוכחנו. יש את ה"סכנה" שאנחנו במקרה היוצא מן הכלל, אבל אז {% equation %}j=0{% endequation %} (כי אסרנו על {% equation %}i{% endequation %} להיות 0) וזה מוביל לסתירה כי אז {% equation %}i=2&gt;1=n{% endequation %}. בקיצור, החריג ההוא לא ממש רלוונטי במקרה הזה.

במקרה השני {% equation %}j&gt;2n{% endequation %}. נסמן {% equation %}t=4n-j{% endequation %}, אז {% equation %}0&lt;t&lt;2n{% endequation %}. כעת, זוכרים שהוכחנו מתישהו ש-{% equation %}x_{4n\pm j}\equiv_{x_{n}}x_{j}{% endequation %}? זה נותן לנו עכשיו ש-{% equation %}x_{t}\equiv_{x_{n}}x_{j}\equiv x_{i}{% endequation %} ולכן שוב, מהמשפט שזה עתה הוכחנו, {% equation %}t=i{% endequation %} (ולמה החריג למשפט לא יכול להתקיים כעת?)

רק עוד דבר אחד וסיימנו: נניח ש-{% equation %}0&lt;i\le n{% endequation %} ומתקיים {% equation %}x_{i}\equiv_{x_{n}}x_{j}{% endequation %}, בלי שום הנחות על {% equation %}j{% endequation %}. מה נוכל לומר עליו? ובכן, בואו ננסה לחלק אותו ב-{% equation %}4n{% endequation %}, כלומר נרשום אותו בצורה {% equation %}j=4nt+r{% endequation %} כאשר {% equation %}0\le r&lt;4n{% endequation %}. עכשיו, זכרו שוב ש-{% equation %}x_{4n\pm k}\equiv_{x_{n}}x_{k}{% endequation %} ושאפשר לכתוב {% equation %}4nt+r=4n+\left(4n\left(t-1\right)+r\right){% endequation %}, ולכן {% equation %}x_{j}=x_{4nt+r}\equiv_{x_{n}}x_{4n\left(t-1\right)+r}{% endequation %}. אפשר להמשיך עם זה ולקבל בסופו של דבר {% equation %}x_{j}\equiv_{x_{n}}x_{r}{% endequation %}, ולכן {% equation %}x_{r}\equiv_{x_{n}}x_{i}{% endequation %}. עכשיו {% equation %}0\le r&lt;4n{% endequation %} ולכן אפשר להשתמש במשפט הקודם עליו ולקבל {% equation %}i=r{% endequation %} או {% equation %}i=4n-r{% endequation %}. משני המקרים הללו נקבל ש-{% equation %}j\equiv_{4n}r\equiv_{4n}\pm i{% endequation %} (אחד משניהם, לא שניהם גם יחד!).

זהו. זה היה מייגע ביותר, אבל עכשיו קיבלנו די והותר כלי נשק להתמודדות עם שאלת הדיופנטיות של {% equation %}\left(x_{n},y_{n}\right){% endequation %} בפרט, ושל הפונקציה האקספוננציאלית בכלל. בפוסט הבא זה גם יקרה בפועל.
